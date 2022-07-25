from django.contrib import admin
from django.urls import path
from whytingapp import views
from accounts import views as accounts_views
<<<<<<< HEAD
from bookapp import views as book_views
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> 0c4514649b991af24cb4505abb93dca13d376e44

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('main',accounts_views.signUp, name="main"),
    path('login/', accounts_views.login, name='login'),
    path('signup', accounts_views.signUp  ,name="signUp"),
    path('logout/', accounts_views.logout, name='logout'),
    path('register_owner/', accounts_views.register_owner, name='register_owner'),
    path('register_customer/', accounts_views.register_customer, name='register_customer'),
<<<<<<< HEAD
    path('divide/', accounts_views.divide, name='divide'),

    # reservation
    path('reservation/', book_views.book, name='book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]
>>>>>>> 0c4514649b991af24cb4505abb93dca13d376e44
