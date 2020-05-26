from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Expense)
admin.site.register(models.Token)

#admin.site.register(models.Income)

@admin.register(models.Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("text","date","user")
