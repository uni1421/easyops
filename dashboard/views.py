from django.shortcuts import render

# Create your views here.

class IndexView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "dashboard/index.html")