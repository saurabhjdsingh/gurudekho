from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.deletion import CASCADE

profession_CHOICES = [
    ('Student', 'Student'),
    ('Tutor', 'Tutor'),
]

SUBSCRIPTION = (
    ('F', 'FREE'),
    ('M','MONTHLY'),
    ('Y', 'YEARLY')
    )

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True,)
    profession = models.CharField(max_length=8, choices=profession_CHOICES, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    birth_day = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="users/profile/%y/%m/%d", default="users/person.png", null=True, blank=True)
    is_pro = models.BooleanField(default=False)
    pro_expiry_date = models.DateTimeField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100, choices=SUBSCRIPTION , default="FREE")

    def __str__(self):
        return self.user.username


class Tutor(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=CASCADE)
    education = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.profile.user.username
        


class Payment(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=CASCADE)
    payment_amount = models.CharField(max_length=200, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_id = models.CharField(max_length=200, null=True, blank=True, unique=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    captured = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.profile.user.username
    