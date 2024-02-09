from django.contrib import admin
from .models import User, Certification, Company, Supplier, ForumPost

admin.site.register(User)
admin.site.register(Certification)
admin.site.register(Company)
admin.site.register(Supplier)
admin.site.register(ForumPost)
