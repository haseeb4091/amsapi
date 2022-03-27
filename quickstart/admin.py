from django.contrib import admin
from .models import Room
from .models import buildings
from .models import addroom
from .models import customeraccount
from .models import allbills
# Register your models here
from .models import Owner
@admin.register(buildings)
class buildingsAdmin(admin.ModelAdmin):
    list_display = ['id','name','address']
@admin.register(Owner)
class buildingsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
@admin.register(addroom)
class roomAdmin(admin.ModelAdmin):
    list_display = ['id','name','building','owner']
@admin.register(customeraccount)
class roomAdmin(admin.ModelAdmin):
    list_display = ['id','name','cnic','phno','role','address','room','rent','security','accountno','debt']
@admin.register(allbills)
class allbillsAdmin(admin.ModelAdmin):
    list_display = ['id','date','accountno','rent','security','bill','remaining','total','paid']
