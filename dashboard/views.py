from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.


class IndexView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "dashboard/index.html")

