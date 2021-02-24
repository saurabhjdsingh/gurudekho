from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from dashboard.models import Profile, Tutor, Payment


class ProfileAdmin(ModelAdmin):
    list_display = ["user", "profession", "subscription_type"]
    search_fields = ["profession", "city"]
    list_filter = ["profession", "is_pro", "subscription_type"]
    
admin.site.register(Profile, ProfileAdmin)


class TutorAdmin(ModelAdmin):
    list_display = ["profile"]
    search_fields = ["profile__user__username"]
    list_filter = ["profile__user__username"]
    
admin.site.register(Tutor, TutorAdmin)


class PaymentAdmin(ModelAdmin):
    list_display = ["profile", "payment_amount"]
    search_fields = ["profile__user__username", "payment_id", "payment_amount", "email", "phone_number"]
    list_filter = ["payment_amount"]
    
admin.site.register(Payment, PaymentAdmin)
