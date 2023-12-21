from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages

from account.forms import SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruyxatdan otdingiz')
            return redirect('login')
        else:
            print(form.errors)
            messages.warning(request, 'Xatolik roy berdi')

    form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/signup.html', context=context)


def logout_view(request):
    logout(request)
    messages.info(request, '✔ User successfully logged outed!')
    return redirect('qiuz')
