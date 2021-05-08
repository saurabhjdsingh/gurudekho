from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from dashboard.models import Profile, Tutor, Payment, faq


class ProfileAdmin(ModelAdmin):
    list_display = ["user", "profession", "subscription_type"]
    search_fields = ["user__username","profession", "city"]
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


class faqAdmin(ModelAdmin):
    list_display = ["faq_title"]
    search_fields = ["faq_title"]
    
admin.site.register(faq, faqAdmin)
