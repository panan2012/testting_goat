from django.http import HttpResponse
from django.shortcuts import redirect,render
from lists.models import Item, List
# from django.http import HttpResponse
# Create your views here.
# home_page = None

def home_page(request):
    # if request.method == "POST":
    #     Item.objects.create(text=request.POST["item_text"])
    #     return redirect("/lists/the-only-list-in-the-world/")
    
    # items = Item.objects.all()
    # return render(request, "home.html", {"items": items})
    return render(request, "home.html")

    # return render(
    #     request,
    #     "home.html",
    #     {"new_item_text": request.POST.get("item_text", "")},
    # )



   # if request.method == "POST":
   #    return HttpResponse("You submitted: " + request.POST["item_text"])
   # return render(request, "home.html")


def view_list(request):
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})


def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect("/lists/the-only-list-in-the-world/")