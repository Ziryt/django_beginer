from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created. You can log in now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uu_form.is_valid() and pu_form.is_valid():
            uu_form.save()
            pu_form.save( )
            messages.success(request, f'Account updated.')
            return redirect('profile')
    else:
        uu_form = UserUpdateForm(instance=request.user)
        pu_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': uu_form,
        'p_form': pu_form
    }

    return render(request, 'users/profile.html', context)
