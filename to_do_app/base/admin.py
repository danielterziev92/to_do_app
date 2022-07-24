from django.contrib import admin

from to_do_app.base.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'day_of_birth')
