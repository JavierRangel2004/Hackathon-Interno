from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Certification, Company, Supplier, ForumPost

# Define a custom UserAdmin
class CustomUserAdmin(UserAdmin):
    model = User
    # Add fieldsets if you want to add fields to the create user form in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_advisor', 'is_company',)}),
    )
    # Add list_display to customize the columns displayed in the user list page
    list_display = ('username', 'email', 'is_staff', 'is_advisor', 'is_company')
    # Add fieldsets to customize the user edit form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_advisor', 'is_company',)}),
    )

# Register the custom UserAdmin
admin.site.register(User, CustomUserAdmin)

# Register other models with default admin interface
admin.site.register(Certification)
admin.site.register(Company)
admin.site.register(Supplier)
admin.site.register(ForumPost)
