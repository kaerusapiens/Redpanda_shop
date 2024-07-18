from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from .forms import UserCreationForm

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

#USER ADMIN作成
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('userid', 'email', 'password',)}),
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
        (None, {'fields': ('userid', 'email', 'password',)}),
    )
    add_form = UserCreationForm
    inlines = (ProfileInline,)

#USER ADMINに紐づくProfileブロック作成
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass