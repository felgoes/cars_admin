from django.contrib import admin

from .models import Vehicle, VehicleModel, Brand, Partner


class PartnerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'document_id']


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class VehicleModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class VehicleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('plate_num',)}
    list_display = ['user', 'plate_num', 'date_created']


admin.site.register(Partner, PartnerAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(VehicleModel, VehicleModelAdmin)
admin.site.register(Vehicle, VehicleAdmin)
