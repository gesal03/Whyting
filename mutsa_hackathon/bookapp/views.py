from django.shortcuts import render, redirect

# Create your views here.
def book(request, store_id):
    # reservation 객체 reserv 생성
    # form 이용해서 reservation seat&time 정보 가져오기
    # 로그인한 사용자 id, 해당 store id 정보 가져오기 - request param?
    
    """
    reserv.save()
    """
    return redirect('home')