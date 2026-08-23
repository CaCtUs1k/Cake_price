from django.contrib import admin
from .models import Cake, RuleSettings, Filling

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')  # Колонки у списку тортів
    search_fields = ('title',)         # Пошук за назвою

@admin.register(RuleSettings)
class RuleSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Забороняємо створювати більше одного запису
        if RuleSettings.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Filling)
class FillingAdmin(admin.ModelAdmin):
    list_display = ('name',)