from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from gurudekho import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
UserModel = get_user_model()


def confirm_your_account(request):
    return render(request, 'accounts/confirm_account.html')


def account_activated(request):
    return render(request, 'accounts/account_activated.html')


def account_activated_false(request):
    return render(request, 'accounts/account_activated_false.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        messages=None
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = True
                user.save()
                # user = form.save(commit=False,)
                # user.is_active = False
                # current_site = get_current_site(request)
                # mail_subject = 'Activate your account.'
                # to_email = form.cleaned_data.get('email')
                # html_content = render_to_string('accounts/activation_mail.html', {
                #     'user': user,
                #     'domain': current_site.domain,
                #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                #     'token': default_token_generator.make_token(user),
                # })
                # text_content = strip_tags(html_content)
                # email = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [to_email])
                # email.attach_alternative(html_content, "text/html")
                # email.send()
                # return redirect('accounts:confirm_your_account')
                username = request.POST.get('username')
                password = request.POST.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return redirect('dashboard:aftersignup')
            else:
                form = SignUpForm()
                messages = "Form is not Valid! "
                return render(request, 'accounts/signup.html', {'form': form, 'messages': messages})
        else:
            form = SignUpForm()
            return render(request, 'accounts/signup.html', {'form': form, 'messages': messages})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('accounts:account_activated')
    else:
        return redirect('accounts:account_activated_false')


def signin(request):
    if request.GET:
        next_page = request.GET['next']
        if request.user.is_authenticated:
            return HttpResponseRedirect(next_page)
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if 'next_page' in locals():
                    return HttpResponseRedirect(next_page)
                else:
                    return redirect('dashboard:aftersignup')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def signout(request):
    logout(request)
    return redirect('accounts:signin')
