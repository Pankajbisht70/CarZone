from django.contrib import admin
from.models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px" />'.format(object.car_photo.url))
    thumbnail.short_description = 'Car Image'

    list_display = ('id','thumbnail','car_title','city','color','model','body_style','is_featured')
    list_display_links = ('car_title','thumbnail',)
    list_editable = ('is_featured',)
    search_fields = ('car_title','city','state')
    list_filter =  ('car_title','city','state')


admin.site.register(Car,CarAdmin)
