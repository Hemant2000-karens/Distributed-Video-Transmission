from django.contrib import admin

# Register your models here.
from django import forms
from .models import ServerTimeZone
import pytz
from .models import BroadcastingInfo

# admin.site.register(BroadcastingInfo)


class BroadcastingInfoAdmin(admin.ModelAdmin):
    list_display = ('broadcast_time', 'timezone', 'video_filename', 'viewers_count', 'video_file') # Customize the display columns

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