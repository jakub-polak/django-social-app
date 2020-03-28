from django.contrib import admin

from accounts.models import UserProfile

admin.site.site_header = 'Administration'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'website', 'phone')

    def user_info(self, obj: UserProfile):
        return obj.description

    def get_queryset(self, request):
        queryset = super().get_queryset(request).order_by('-phone', 'user')
        return queryset

    user_info.short_description = 'info'


admin.site.register(UserProfile, UserProfileAdmin)
