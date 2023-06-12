from django.shortcuts import render, HttpResponse
import requests
from .models import Slider

NEST_SERVER_URI = "http://localhost:3000"
PAGE_DATA_COUNT = "3"

# Create your views here.


def home(request):
    slider_data = Slider.objects.all()
    print(type(slider_data))
    print(list(j.image for j in slider_data))
    context = {
        "slider": slider_data
    }
    return render(request=request, template_name="objects/index.html", context=context)


def magazin(request, type, categorie, region, page):
    print(request.GET)
    print(request.POST)
    INVERSE_URL = "/".join(["/magazin", type, "P" if categorie == "R" else "R", region, page])
    NEXT_URL = "/".join(["/magazin", type, categorie, region, str(int(page) + 1)])
    PREV_URL = "/".join(["/magazin", type, categorie, region, str(int(page) - 1)])  if int(page) > 1 else ""
     
    if type != "noType":
        r = requests.get(f'{NEST_SERVER_URI}/object/getObjectByType/{type}/{categorie}/{region}/{PAGE_DATA_COUNT}/{page}')
    else:
        r = requests.get(f'{NEST_SERVER_URI}/object/getAllRecoverAndLoseObject/{categorie}/{region}/Aucune/{PAGE_DATA_COUNT}/{page}')
        print(r.json())
    result = r.json()

    return render(request=request, template_name="objects/magazincontent.html", context={"types": get_list_object_accueil(), "datas": result, "NEXT_URL": NEXT_URL, "PREV_URL": PREV_URL, "INVERSE_URL": INVERSE_URL, "SELECTED_CATEGORY": categorie, "selected_type": type if type != "noType" else region})


def magazin_content(request):
    return render(request=request, template_name="objects/magazincontent.html")


def getObjectByCategorie(request, categorie, selected_type):
    INVERSE_URL = "/".join(["/getObjectByCategorie", "P" if categorie == "R" else "R"])
    r = requests.get(f'{NEST_SERVER_URI}/object/getObjectByCategorie/{categorie}')
    result = r.json()
    return render(request=request, template_name="objects/magazincontent.html", context={"types": get_list_object_accueil(), "datas": result, "INVERSE_URL": INVERSE_URL, "SELECTED_CATEGORY": categorie, "selected_type": selected_type})



def get_list_object_accueil():
    r = requests.get(f'{NEST_SERVER_URI}/object/getObjectType')
    return r.json()


def recherche(request, searchInput, page):

    formSearchInput = request.GET.get("searchInput")
    if searchInput == "None":
        r = requests.get(f'{NEST_SERVER_URI}/object/getSearchResult/{formSearchInput}/{PAGE_DATA_COUNT}/{page}')
        NEXT_URL = f"/recherche/{formSearchInput}/{int(page) + 1}"
        PREV_URL = f"/recherche/{formSearchInput}/{int(page) - 1}" if int(page) > 1 else "" 
    else:
        r = requests.get(f'{NEST_SERVER_URI}/object/getSearchResult/{searchInput}/{PAGE_DATA_COUNT}/{page}')
        NEXT_URL = f"/recherche/{searchInput}/{int(page) + 1}"
        PREV_URL = f"/recherche/{searchInput}/{int(page) - 1}" if int(page) > 1 else ""
    result = r.json()
    return render(request=request, template_name="objects/magazincontent.html", context={"types": get_list_object_accueil(), "datas": result, "NEXT_URL": NEXT_URL, "PREV_URL": PREV_URL , "selected_type": "Resultat pour"})
