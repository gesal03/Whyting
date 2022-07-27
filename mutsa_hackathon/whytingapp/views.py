from django.forms import modelform_factory
from django.shortcuts import redirect, render
from forms import ImageForm, StoreForm
from models import Image

def home(request):
    return render(request, 'index.html')

# Seat, Time 객체 생성

def newstore(request):
    # 하나의 modelform 을 여러번 쓸 수 있음. 모델, 모델폼, 몇 개의 폼을 띄울건지 갯수 
    ImageFormSet = modelform_factory(Image,form=ImageForm, extra=5)
    if request.method == 'POST':
        storeForm = StoreForm(request.POST)
        # queryset 을 none 으로 정의해서 이미지가 없어도 되도록 설정. none 은 빈 쿼리셋 리턴
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())
    
        # 두 모델폼의 유효성 검사를 해주고
        if storeForm.is_valid() and formset.is_valid():
            store_form = storeForm.save(commit=False)
            # storeform user 에 현재 요청된 user 를 담아서 
            store_form.owner_id = request.user
            # 저장. 이 작업 안하면 user null error
            store_form.save()
            # 유효성 검사가 왼료된 formset 정리된 데이터 모음
            for form in formset.cleaned_data:
                if form:
                    # image file 
                    image = form['image']
                    print(form)
                    print(form['image'])
                    # post, image file save
                    photo = Image(store_id=store_form, image=image)
                    photo.save()
            # index url 로 요청보냄
            return redirect('home')
    else:
        # POST 요청이 아닌 경우 
        storeForm = StoreForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    
    return render(request, 'newstore.html',
                  {'storeForm': StoreForm, 'formset': formset})