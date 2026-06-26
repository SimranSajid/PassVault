from django.contrib import admin
from .models import PasswordEntry

@admin.register(PasswordEntry)
class PasswordEntryAdmin(admin.ModelAdmin):
    list_display = ('website', 'category', 'user', 'created_at', 'updated_at')
    search_fields = ('website', 'category')
    list_filter = ('category',)