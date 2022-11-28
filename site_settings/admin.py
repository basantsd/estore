from django.contrib import admin
from .models import HomeBanner,BestProduct, SiteSetting
from core.base.admin import BaseAdmin


@admin.register(HomeBanner)
class HomeBannerAdmin(BaseAdmin):
    list_display = ['maintitle','title','small_description','is_active']
    
    
@admin.register(BestProduct)
class BestProductAdmin(BaseAdmin):
    list_display = ['title','tag','is_active']
    

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['name']