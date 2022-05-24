from django.urls import path
from .views import HomeBlogList

app_name = 'blog'

urlpatterns = [
    path('', HomeBlogList.as_view(), name='home'),
    

]
