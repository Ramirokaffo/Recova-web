from django.urls import path
from authentification.views import home, register, log_out, log_in, activate 

urlpatterns = [
    path('auth', home, name="home"),
    path('register', register, name="register"),
    path('login', log_in, name="login"),
    path('logout', log_out, name="logout"),
    path('activate/<uidb64>/<token>', activate, name="activate"),
    # path('update/<int:my_id>', modifier, name="update"),
    # path('delete/<int:my_id>', delete_product, name="delete"),

]
