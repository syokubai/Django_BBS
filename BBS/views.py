from django.shortcuts import render
from django.views import View
from django.contrib import messages


# Create your views here.

class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "BBS/menu.html")


menu = MenuView.as_view()
