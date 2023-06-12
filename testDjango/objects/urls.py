from django.urls import path
from objects.views import *

urlpatterns = [
    path('object', home, name="object"),
    path('magazin/<type>/<categorie>/<region>/<page>', magazin, name="magazin"),
    path('magazinContent', magazin_content, name="magazinContent"),
    path('getObjectByCategorie/<categorie>/<selected_type>', getObjectByCategorie, name="getObjectByCategorie"),
    path('recherche/<searchInput>/<page>', recherche, name="recherche"),
    # path('update/<int:my_id>', modifier, name="update"),
    # path('delete/<int:my_id>', delete_product, name="delete"),

]
