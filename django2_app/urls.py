from django2_app import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.users,name='users')
]