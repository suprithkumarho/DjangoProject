from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UserDetails
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if not UserDetails.objects.filter(email=email).exists():
            new_user = UserDetails(username=username, email=email, password=password)
            new_user.save()

            return redirect('login')

    return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email)

            if user.password == password:
                return render(request, 'success.html', {'user': user})
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password.'})
            
        except UserDetails.DoesNotExist:
            return render(request, 'login.html', {'error': 'User  not exist'})

    return render(request, 'login.html')

def get_all_users(request):
    users_list = UserDetails.objects.all()

    return render(request, 'all_users.html', {'users': users_list})



def get_user_by_email(request, email):
    user_detail = get_object_or_404(UserDetails, email=email)

    return render(request, 'user_detail.html', {'user': user_detail})


@csrf_exempt
def update_user(request, username):
    user_to_update = get_object_or_404(UserDetails, username=username)

    if request.method == 'POST':
        user_to_update.email = request.POST['email']
        user_to_update.password = request.POST['password']
        user_to_update.save()
        return redirect('all_users')
    
    return render(request, 'update_user.html', {'user': user_to_update})

@csrf_exempt
def delete_user(request, email):

    user_to_delete = get_object_or_404(UserDetails, email=email)
    
    if request.method == 'POST':
        user_to_delete.delete()
        return redirect('all_users')
    
    return render(request, 'confirm_delete.html', {'user': user_to_delete})
