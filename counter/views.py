from django.shortcuts import render
from django.views import View


# Create your views here.


class Index(View):
    def get(self, request):
        context = {
            'count': "hello worlds"
        }
        return render(request, 'counter/index.html', context)
