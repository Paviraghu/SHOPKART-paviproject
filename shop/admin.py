from atexit import register
from django.contrib import admin
from .models import *

"""
class CatogoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
    admin.site.register(Catagory,CatogoryAdmin)
"""

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
