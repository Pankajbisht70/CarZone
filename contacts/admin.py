from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','city')
    list_display_links = ('id','first_name')
    list_per_page = 25
    search_fields = ('car_title','first_name','last_name','email')
    list_filter =  ('car_title','city','state')


admin.site.register(Contact,ContactAdmin)