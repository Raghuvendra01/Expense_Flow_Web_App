from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Validation checks
        if not full_name or not email or not password or not confirm_password:
            messages.error(request, 'All fields are required.')
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return redirect('register')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'This account already exists.')
            return redirect('register')
        
        try:
            # Create new user
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name.split()[0] if full_name else '',
                last_name=' '.join(full_name.split()[1:]) if len(full_name.split()) > 1 else ''
            )
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('register')
    
    else:
        return render(request, 'register.html')
    

#login
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        # Validation
        if not email or not password:
            messages.error(request, 'Email and password are required.')
            return redirect('login')
        
        # Authenticate user (Django's User model uses 'username' field)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Login successful
            auth_login(request, user)
            # messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('dashboard')
        else:
            # Authentication failed
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
    
    else:
        # GET request - show login form
        return render(request, 'index.html')
