from django import forms
from .models import Reservation

class ReservForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('reservation_time','reservation_seat')
        labels = {
            'reservation_time': _('예약 시간'),
            'reservation_seat': _('예약 자리')
        }