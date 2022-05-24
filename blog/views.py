from django import views
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class HomeBlogList(View):
    
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_list.html', context )

