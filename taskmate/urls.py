
from django.contrib import admin
from django.urls import path,include
from mylist_app import views as mylist_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mylist_views.index, name='index'),
    path('myap/', include('mylist_app.urls')),
    path('account/', include('users_app.urls')),
    path('about', mylist_views.about, name='about'),
    path('contact', mylist_views.contact, name='contact')

   
]
