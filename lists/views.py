from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
# home_page = None

def home_page(request):
   return render(
        request,
        "home.html",
        {"new_item_text": request.POST.get("item_text", "")},
    )



   # if request.method == "POST":
   #    return HttpResponse("You submitted: " + request.POST["item_text"])
   # return render(request, "home.html")
