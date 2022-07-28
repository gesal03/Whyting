from django.shortcuts import render, redirect

from .models import Reservation

# Create your views here.
def book(request, store_id):
    if request.POST == "POST":
        # reservation 객체 reserv 생성
        # form 이용해서 reservation seat&time 정보 가져오기
        # 로그인한 사용자 id, 해당 store id 정보 가져오기 - request param?
        current_user = request.user.id
        current_store = store_id
        current_seat = request.POST['seat']
        current_time = request.POST['time']
        reserv = Reservation(store_id=current_store, customer_id=current_user, seat_id=current_seat, time_id=current_time)
        reserv.save()
        
        return redirect('home')