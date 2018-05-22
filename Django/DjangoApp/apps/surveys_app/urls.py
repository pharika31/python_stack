from django.conf.urls import url
from . import views
urlpatterns =[
 url(r'^$',views.surveys),
 url(r'^new/$',views.new),
]
