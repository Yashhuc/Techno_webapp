from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email.endswith('@nituktech.ac.in'):
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Your account has been created!')
                return redirect('login')
            else:
               messages.warning(request, 'Please register with a valid nituk email address.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
