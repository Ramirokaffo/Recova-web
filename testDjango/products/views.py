import os.path

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
# from django.urls import Http404
from .models import Products
from .form import ProductCreateForm, RowProductForm


def home(request, *args, **kwargs):
    print(request.user)
    print(args)
    print(kwargs)
    name = "ramiro"
    number = 55
    mylist = [0, 3, 9, 49, 7, 1]
    context = {"nom": name, "numero": number, "maliste": mylist}
    images = ["images/site-ebs/header-bg/IMG_7972.JPG", 
              "images/site-ebs/header-bg/Background.jpg", 
              "images/site-ebs/bp/bp1.JPG", 
              "images/site-ebs/header-bg/IMG_8105.JPG",
              "images/site-ebs/header-bg/IMG_8106.JPG",
              "images/site-ebs/bp/bp2.JPG",
              "images/site-ebs/sw/SWI1.JPG"
              ]
    products = Products.objects.all()
    images = list(e.image for e in products)
    print(list(e.image for e in products))
    return render(request, "site-ebs/index.html", {"images": images})

 
def contact(request):
    return render(request, "contacts.html")


def blog(request):
    return HttpResponse("Blog page")


def product_list(request):
    # product = Products.objects.get(id=5)
    products = Products.objects.all()
    print(list(e.image for e in products))
    context = {
        "products": products,
    }

    return render(request, "product/details.html", context)


def product_create(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    message = "Le produit a été bien reçu"
    return render(request, "product/create.html", {"form": form, "message": message})


def modifier(request, my_id):
    message = "Modification echouée"
    products = Products.objects.all()
    print(list(e.id for e in products))
    obj = get_object_or_404(Products, id=my_id)

    # try:
    #     obj = Products.objects.get(id=my_id)
    #
    # except Products.DoesNotExist:
    #     raise Http404
    form = ProductCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
        message = "Le produit a été bien modifié"
    return render(request, "product/update.html", {"form": form, "message": message})


def delete_product(request, my_id):
    obj = get_object_or_404(Products, id=my_id)
    name = obj.name
    if request.POST:
        obj.delete()
        return redirect("product")
    return render(request, "product/delete.html", {"name": name})

# def product_create(request):
#     message = "Echec de l'enregistrement"
#
#
#     if request.POST:
#         # print(request.POST.get("image"))
#         print(request.POST)
#         print(str(request.FILES["image"]))
#
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         price = request.POST.get("price")
#         image = os.path.join("images/", str(request.FILES["image"]))
#         # os.open()
#         slug = request.POST.get("slug")
#         new_product = Products.objects.create(name=name, description=description, price=price, image=image, slug=slug)
#         new_product.save()
#         print(request.POST["name"])
#         print(request.POST["description"])
#         print(request.POST["price"])
#         print(request.GET)
#         message = "Produit enregistré avec succes"
#     return render(request, "product/create.html", {"message": message})

# def product_create(request):
#     # return
#     form = RowProductForm()
#     # print(request.FILES)
#     # print(request.FILES["image"])
#     # request.POST["image"] = request.FILES["image"]
#     # print(type(request.FILES["image"]))
#     # print(request.FILES)
#     message = "Echec de l'enregistrement"
#     if request.POST:
#         # print(str(request.FILES["image"]))
#         form = RowProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             new_product = Products.objects.create(**form.cleaned_data)
#             # new_product.save()
#             form = RowProductForm()
#             message = "Produit sauvegardé avec succes"
#     return render(request, "product/create.html", {"form": form, "message": message})
