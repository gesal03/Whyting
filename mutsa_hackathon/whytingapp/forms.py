from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Store, Image


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'introduction', 'address', 'number', 'start_time', 'end_time' )
        labels = {
            'name': _('가게 이름'),
            'introduction':_('가게 소개'),
            'address': _('가게 주소'),
            'number': _('가게 전화번호'),
            'start_time': _('영업 시작 시간'),
            'end_time': _('영업 종료 시간')
        }
 
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image 
        fields = ('image', )
        labels = {
            'image': _('가게 사진'),
            
        }