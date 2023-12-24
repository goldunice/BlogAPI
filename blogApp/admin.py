from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ['id', 'sarlavha', 'matn', 'sana', 'muallif', 'korish_soni']
    list_filter = ['sana', 'muallif']


class MuallifAdmin(UserAdmin):
    model = Muallif
    fieldsets = UserAdmin.fieldsets + (
        ('Muallif', {'fields': ('ism', 'yosh', 'kasb')}),)
    list_display = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',
                    'is_superuser']


admin.site.register(Muallif, MuallifAdmin)
