from django.urls import path
from products.views import home, blog, contact, product_list, product_create, modifier, delete_product

urlpatterns = [
    path('', home, name="home"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('product/', product_list, name="product"),
    path('create/', product_create, name="create"),
    path('update/<int:my_id>', modifier, name="update"),
    path('delete/<int:my_id>', delete_product, name="delete"),

]



