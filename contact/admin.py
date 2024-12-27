from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email', 'show')
  ordering = ('id', )
  #list_filter = ('created_date', )
  search_fields = ('id', 'first_name', 'last_name')
  list_per_page = 100
  list_max_show_all = 500
  list_editable = ('first_name', 'show')
  list_display_links = ('id', )
  
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', )
  
  
  