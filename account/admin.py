from django.contrib import admin
from .forms import UserCreationForm
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('userid','email', 'password',)}),
        (None, {'fields': ('is_admin',)}),
    )
    list_display = (
        'userid',
        'email',
        'is_admin',
    )
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    add_fieldsets = (
         (None, {'fields': ('userid','email', 'password',)}),
    )
    add_form = UserCreationForm
    inlines = (ProfileInline,)




admin.site.register(User, UserAdmin)
admin.site.register(Profile)

