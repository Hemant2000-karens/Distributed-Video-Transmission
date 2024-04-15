from django.contrib import admin

# Register your models here.
from django import forms
from .models import ServerTimeZone
import pytz
from .models import BroadcastingInfo
import uuid
# admin.site.register(BroadcastingInfo)


class BroadcastingInfoAdmin(admin.ModelAdmin):
    list_display = ('broadcast_time', 'timezone', 'video_filename', 'viewers_count')  # Customize the display columns # Keep only relevant fields in list_display
    def save_model(self, request, obj, form, change):
        if not obj.video_id:  # Generate video ID if not provided
            obj.video_id = str(uuid.uuid4())
        super().save_model(request, obj, form, change)

admin.site.register(BroadcastingInfo, BroadcastingInfoAdmin)

class ServerTimeZoneAdminForm(forms.ModelForm):
    class Meta:
        model = ServerTimeZone
        fields = '__all__'
        widgets = {
            'timezone': forms.Select(choices=[(tz, tz) for tz in pytz.all_timezones]),
        }

class ServerTimeZoneAdmin(admin.ModelAdmin):
    form = ServerTimeZoneAdminForm

admin.site.register(ServerTimeZone, ServerTimeZoneAdmin)