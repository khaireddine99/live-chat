from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from chat.models import Message

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "gender", "is_staff", "gay"]
    list_filter = ["is_staff", "is_superuser", "is_active", "gender", "gay"]
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender', "gay")})
    )

    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)
