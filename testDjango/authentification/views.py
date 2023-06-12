from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from djangoProject import settings
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .token import generatorToken
import requests

NEST_SERVER_URI = "http://localhost:3000"

# Create your views here.


def home(request):
    r = requests.get(f'{NEST_SERVER_URI}/object/getObjectType')

    # print(r.status_code)
    # print(r.headers)
    print(r.text)
    return render(request, "authentification/index.html")

def register(request):
    if request.POST:
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        email = request.POST.get("email")

        if User.objects.filter(username=username):
            messages.error(request, "Ce nom d'utilisateur est deja utilisé")
            return redirect("register")
        
        # if User.objects.filter(email=email):
        #     messages.error(request, "Cette adresse email a deja un compte")
        #     return redirect("register")

        if not username.isalnum():
            messages.error(request, "Le nom doit etre alphanumerique")
            return redirect("register")
        
        if password != password1:
            messages.error(request, "Mot de passe non correspondant !")
            return redirect("register")



        print(username, firstname, lastname, password, password1, email)
        myUser = User.objects.create_user(username=username, email=email, password=password)
        myUser.first_name = firstname
        myUser.last_name = lastname
        myUser.is_active = False
        # myUser.save()
        messages.success(request, "Votre compte a été créé avec succès !")
        subject = "Bienvenue sur notre application"
        message = f"Bienvenue {myUser.first_name} {myUser.last_name} \n Nous sommes heureux de vous compter parmi nous \n\n\n Merci ! \n\n Ramiro Kaffo"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myUser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        
        current_site = get_current_site(request)
        confirm_subject = "Confirmation de l'adresse email"
        confirm_maessage = render_to_string("email_confirm.html", {
            "name": myUser.first_name,
            "domain":current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(myUser.pk)),
            "token": generatorToken.make_token(myUser),
        })
        email = EmailMessage(
            confirm_subject,
            confirm_maessage,
            settings.EMAIL_HOST_USER,
            [myUser.email]
        )

        email.fail_silently = False
        email.send()
        
        return redirect("login")
    
    return render(request, "authentification/register.html")

def log_in(request):
    firstname = ""

    if request.POST:
        print("Oui la methode c'est post")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        my_user = User.objects.get(username=username)

        if user is not None:
            print("Non c'est pas none")
            login(request, user)
            firstname = user.first_name
            # messages.success(request, "Authentification reussie")
            return render(request, "authentification/index.html", {"firstname": firstname})
        elif my_user.isinstance == False:
            messages.error(request, "Vous n'avez pas encore activé votre compte; veuillez verifier votre adresse email")
        else:
            print("Oui c'est none")
            messages.error(request, "Mauvaise authentification")
            return redirect("login")
    else:
        print("Non la methode c'est pas post")
        return render(request, "authentification/login.html", {"firstname": firstname})
        # return redirect("login")

def log_out(request):
    logout(request)
    messages.success(request, "Deconnexion effectuée avec succes !")
    return redirect("home")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and generatorToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Votre compte a bien été activé felicitation ! connectez-vous maintenant")
        return redirect("login")
    else:
        messages.error(request, "Votre compte n'a pas pu etre activé; veuillez reésayer")
        return redirect("home")
