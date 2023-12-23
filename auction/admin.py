from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "is_publish"]
    list_editable = ["is_publish"]


@admin.register(Comment)
class ListingAdmin(admin.ModelAdmin):
    list_display = ["author", "listing_id"]


admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(WatchList)
