from django.http import HttpResponse
from django.shortcuts import redirect,render
from lists.models import Item
# from django.http import HttpResponse
# Create your views here.
# home_page = None

def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/")
    
    items = Item.objects.all()
    return render(request, "home.html", {"items": items})


    # return render(
    #     request,
    #     "home.html",
    #     {"new_item_text": request.POST.get("item_text", "")},
    # )



   # if request.method == "POST":
   #    return HttpResponse("You submitted: " + request.POST["item_text"])
   # return render(request, "home.html")
