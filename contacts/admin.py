from django.contrib import admin
from .models import Contact, PhoneNumber

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1  # Number of empty forms to display

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'company', 'user')
    inlines = [PhoneNumberInline]
    search_fields = ('first_name', 'last_name', 'address', 'company')
    list_filter = ('user',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(PhoneNumber)
