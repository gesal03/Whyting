from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Store, Image


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'introduction', 'address', 'number' )
        labels = {
            'name': _('가게 이름'),
            'introduction':_('가게 소개'),
            'address': _('가게 주소'),
            'number': _('가게 전화번호')
        }
 
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image 
        fields = ('image', )
        labels = {
            'image': _('가게 사진'),
            
        }