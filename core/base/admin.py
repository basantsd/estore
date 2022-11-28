from django.contrib import admin
from django.contrib import messages
  
class BaseAdmin(admin.ModelAdmin):
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
  
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active = 1)
        messages.success(request, "Selected Record(s) Active Successfully !!")
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected Record(s) Inactive Successfully !!")
  
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")
  