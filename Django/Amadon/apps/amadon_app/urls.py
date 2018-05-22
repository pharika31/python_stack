from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$',views.index),
    url(r'^buy$',views.buy),
    url(r'^checkout$',views.checkout),
    url(r'^clear$',views.clear)
]
