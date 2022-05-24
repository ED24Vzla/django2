from django.urls import path
from .views import HomeBlogList, BlogCreateView

app_name = 'blog'

urlpatterns = [
    path('', HomeBlogList.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),

]
