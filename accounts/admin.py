from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ["id", "username", "email", "gender", "is_staff", "gay"]
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'gender', "gay")})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'gender', 'gay', 'password1', 'password2'),
        }),
    )

    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(Post)

