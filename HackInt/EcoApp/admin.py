# admin.py
from django.contrib import admin
from .models import User, Company, Advisor, Sector, Specialty, Certification, ForumPost
from django.contrib.auth.admin import UserAdmin

# Custom UserAdmin to include 'is_advisor' and 'is_company' flags
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_advisor', 'is_company', 'is_staff', 'is_active',)
    list_filter = ('is_advisor', 'is_company', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_advisor', 'is_company', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_advisor', 'is_company')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)

# Registering models on the admin site
admin.site.register(User, CustomUserAdmin)
admin.site.register(Company)
admin.site.register(Advisor)
admin.site.register(Sector)
admin.site.register(Specialty)
admin.site.register(Certification)
admin.site.register(ForumPost)
