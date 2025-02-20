from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email', 'age')}),
    #     ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('تاریخ‌ها', {'fields': ('last_login', 'date_joined')}),
    # )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'email', 'password1', 'password2', 'age')}
    #     ),
    # )


admin.site.register(CustomUser, CustomUserAdmin)
