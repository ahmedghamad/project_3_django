from django.contrib import admin
from .models import Portfolio

# Register your models here.

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','created_on')
    readonly_fields = ('book_title','description',)