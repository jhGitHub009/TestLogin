from django.contrib import admin

# Register your models here.
from .models import *

# class PalletInline(admin.StackedInline):
# 	model = Pallet
# 	extra = 2

# class MaterialInline(admin.StackedInline):
# 	model = Material
# 	extra = 2

# class IncomingAdmin(admin.ModelAdmin):
# 	inlines = [PalletInline, MaterialInline]

admin.site.register(Material)
admin.site.register(Pallet)
admin.site.register(Zone)
admin.site.register(Outgoing)
admin.site.register(Incoming)
admin.site.register(Unit)
admin.site.register(Packing)