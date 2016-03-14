from django.contrib import admin
from menu.models import Restaurant,Food
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name','phone_number','address')
	search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
	list_display = ('name','restaurant','price','image')
	list_filter = ('is_spicy')
	fields = ('price','restaurant')
	ordering = ('-price')

admin.site.register(Restaurant)
admin.site.register(Food)