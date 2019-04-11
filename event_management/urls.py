from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SignupPageView.as_view(), name='register'),
    url(r'^signup', views.SignupPageView.as_view(), name='register'),
    url(r'^signin', views.SigninPageView.as_view(), name='login'),
    url(r'^dashboard', views.register_user, name='dashboard'),
    
    # url(r'db', views.dashboard, name='dashboard'),
    url(r'events', views.event, name='events')
]
