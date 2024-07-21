from django.contrib import admin
from app.models import *
from django.contrib.auth.admin import UserAdmin
from app.forms import UserCreationForm, ProductForm



#カテゴリーAdmin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # createの際にautofillで作成されて便利
    list_display = ('id','name', 'slug', 'parent')
    list_filter = ('parent',)
    search_fields = ('id','name', 'slug')

#Product ーAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price','product_description', 'can_return','est_ship_date')
    prepopulated_fields = {'slug': ('product_name',)}
    #SELECT ANLY AMONG LEAF SUBCATEGORIES
    form = ProductForm

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