from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "is_ta"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("is_ta",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("is_ta",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
