from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .middlewares import auth, guest

def aboutUs1(request):
    return HttpResponse("hai")


def index(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        otp = request.POST.get('otp')
        referral_code = request.POST.get('referal_code', '')  # Default to empty string if not provided

        # Printing the form values
        print("Phone Number:", phone_number)
        print("Password:", password)
        print("OTP:", otp)
        print("Referral Code:", referral_code)

        # Constructing the response with the form values
        response = (
            f"Phone Number: {phone_number}<br>"
            f"Password: {password}<br>"
            f"OTP: {otp}<br>"
            f"Referral Code: {referral_code}<br>"
        )

        # Returning the response
        return HttpResponse(response)

    return render(request, 'index.html')

def sign_invite(request):

    return render(request, "index.html")



@auth
def dash(request):

    return render(request, "dash.html")


def logout_page(request):
    logout(request)
    return redirect("hai")
@auth
def login_process(request):
    if request.method == "POST":
        # Retrieve values of specific fields from the POST request
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        password = request.POST.get("password")

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("hai")  # Redirect back to the same page

        # Create a new user if the username doesn't exist
        new_user = User.objects.create(
            username=username, first_name=first_name
        )
        new_user.set_password(password)
        new_user.save()

        messages.success(request, "User created successfully")
        return redirect("hai")  # Redirect to a different page

    return render(request, "index.html")

@guest
def login_process_2(request):
    if request.method == "POST":
        # Retrieve values of specific fields from the POST request
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.success(request, " invalid pass")
            return redirect("hai")

        else:
            login(request, user)
            return redirect("dash")

    return render(request, "index.html")

def sign_invitew(request):

    return render(request, "indexc.html")
