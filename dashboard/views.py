from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Tutor, Payment
from .forms import ProfileUpdateForm
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import razorpay
client = razorpay.Client(auth=("rzp_test_ALgOPQkNZjhmdJ", "gWJofbxymxYZVZZDjKQyOTNJ"))
UserModel = get_user_model()


@login_required
def aftersignup(request):
    if Profile.objects.filter(user__id=request.user.id).exists() and Tutor.objects.filter(profile__user=request.user).exists():
        return redirect('dashboard:tutors')
    elif Profile.objects.filter(user__id=request.user.id).exists():
        return redirect('dashboard:editprofile')
    else:
        if request.method == "POST":
            number = request.POST["phone_number"]
            profession = request.POST["profession"]
            city = request.POST["city"]
            date = request.POST["birth_day"]
            p = Profile(user=request.user, phone_number=number, profession=profession, city=city, birth_day=date)
            p.save()
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if p_form.is_valid():
                p_form.save()
            return redirect('dashboard:editprofile')
        else:
            message = "Please fill this form!"
        return render(request, 'dashboard/aftersignup.html', {'message': message})
        
@login_required
def editprofile(request):
    if Profile.objects.filter(user=request.user).exists():
        user_profile = Profile.objects.get(user=request.user)
        if user_profile.profession == "Tutor":
            if request.method == "POST":
                education = request.POST["education"]
                experience = request.POST["experience"]
                about = request.POST["about"]
                if Tutor.objects.filter(profile__user=request.user).exists():
                    tutor = Tutor.objects.get(profile__user=request.user)
                    tutor.education = education
                    tutor.experience = experience
                    tutor.about = about
                    tutor.save()
                else:    
                    p = Tutor(profile=user_profile, education=education, experience=experience, about=about)
                    p.save()
                return redirect('dashboard:tutors')
            else:
                messages = "Please fill this form!"
                if Tutor.objects.filter(profile__user=request.user).exists():
                    tutor = Tutor.objects.get(profile__user=request.user)
                    return render(request, 'dashboard/editprofile.html', {'message': messages, "tutor": tutor})
                else:
                    return render(request, 'dashboard/editprofile.html', {'message': messages})
        else:
            return redirect('dashboard:tutors')
    else:
        return redirect('dashboard:aftersignup')
        
        
@login_required
def tutors(request):
    if request.method == "POST":
        profileList = Profile.objects.filter(profession="Tutor", city=request.POST["city"]).order_by("-id");
        return render(request, 'dashboard/tutors.html', {'profile': profileList, 'city':request.POST["city"]})
    else:
        pass
    return render(request, 'dashboard/tutors.html')
    

@login_required
def detail(request,username):
    person = Profile.objects.get(user=request.user)
    if person.is_pro is True:
        if timezone.now() >= person.pro_expiry_date:
            person.is_pro = False
            person.pro_expiry_date = None
            person.subscription_type = 'F'
            person.save()
    if Profile.objects.filter(user__username=username).exists():
        user_profile = Profile.objects.get(user__username=username)
        if Tutor.objects.filter(profile=user_profile).exists():
            tutor = Tutor.objects.get(profile=user_profile)
            return render(request, 'dashboard/tutor_detail.html', {'tutor': tutor})
        else:
            messages = "Sorry! " + username + "'s Tutor profile is restricted."
            return render(request, 'dashboard/tutor_detail.html', {'message': messages})
    else:
        messages = "Sorry! we are not able to find any tutor in our records with the username " + username
        return render(request, 'dashboard/tutor_detail.html', {'message': messages})


def pro_member(request):
    if request.method == "POST":
        if request.POST['amount'] == "MONTHLY":
            amount = int(117)
        elif request.POST['amount'] == "YEARLY":
            amount = int(1168)
        else:
            amount = int(0)
        payment_id = request.POST.get('razorpay_payment_id')
        payment_amount = amount*100
        client.payment.capture(payment_id, payment_amount, {"currency": "INR"})
        pay = client.payment.fetch(payment_id)
        pay_email = pay.get('email')
        pay_contact = pay.get('contact')
        profile = Profile.objects.filter(user=request.user).first()
        if payment_amount == 11700:
            profile.subscription_type = 'M'
            profile.is_pro = True
            expiry = timezone.now() + timedelta(30)
            profile.pro_expiry_date = expiry
            profile.save()
            pay = Payment(profile=profile, payment_amount=payment_amount, payment_date=timezone.now(), payment_id=payment_id, email=pay_email, phone_number=pay_contact, captured=pay.get('captured'))
            pay.save()
        elif payment_amount == 116800:
            profile.subscription_type = 'Y'
            profile.is_pro = True
            expiry = timezone.now() + timedelta(365)
            profile.pro_expiry_date = expiry
            profile.save()
            pay = Payment(profile=profile, payment_amount=payment_amount, payment_date=timezone.now(), payment_id=payment_id, email=pay_email, phone_number=pay_contact, captured=pay.get('captured'))
            pay.save()
        return redirect('dashboard:tutors')
    return render(request, 'dashboard/pro_member.html')


@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.profession == "Tutor":
        tutor = True
    else:
        tutor = False
    return render(request, 'dashboard/profile.html', {'tutor': tutor})