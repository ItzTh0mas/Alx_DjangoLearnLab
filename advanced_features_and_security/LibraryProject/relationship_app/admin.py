from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser# type: ignore


class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the CustomUser model.
    Extends Django's built-in UserAdmin to handle additional fields.
    """

    # Fields to display in the user list view
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'date_of_birth',
        'age_display',
        'is_active',
        'is_staff',
        'date_joined',
        'profile_photo_display'
    )

    # Fields that can be used to filter the user list
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'date_joined',
        'date_of_birth'
    )

    # Fields that can be searched
    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name'
    )

    # Default ordering
    ordering = ('email',)

    # Fields to display when viewing/editing a user
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
                'date_of_birth',
                'profile_photo'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Fields to display when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'date_of_birth',
                'profile_photo',
                'is_active',
                'is_staff'
            ),
        }),
    )

    # Read-only fields
    readonly_fields = ('date_joined', 'last_login')

    def age_display(self, obj):
        """
        Display the user's age in the admin list view.
        """
        age = obj.age
        if age is not None:
            return f"{age} years old"
        return "Not specified"
    age_display.short_description = "Age"# type: ignore
    age_display.admin_order_field = 'date_of_birth'# type: ignore

    def profile_photo_display(self, obj):
        """
        Display a small version of the profile photo in the admin list view.
        """
        if obj.profile_photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.profile_photo.url
            )
        return "No photo"
    profile_photo_display.short_description = "Profile Photo"# type: ignore

    def get_form(self, request, obj=None, **kwargs):# type: ignore
        """
        Customize the form used in the admin interface.
        """
        form = super().get_form(request, obj, **kwargs)

        # Add help text for custom fields
        if 'date_of_birth' in form.base_fields:# type: ignore
            form.base_fields['date_of_birth'].help_text = "Format: YYYY-MM-DD"# type: ignore

        if 'profile_photo' in form.base_fields:# type: ignore
            form.base_fields['profile_photo'].help_text = "Upload an image file (JPG, PNG, etc.)"# type: ignore

        return form

    def save_model(self, request, obj, form, change):
        """
        Custom save method to handle any special logic when saving users.
        """
        super().save_model(request, obj, form, change)

        # Add any custom logic here if needed
        # For example, sending welcome email to new users
        if not change:  # This is a new user
            # You could add logic here to send welcome email
            pass


# Register the CustomUser model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)

# Optional: Customize admin site headers
admin.site.site_header = "Advanced Features Admin"
admin.site.site_title = "Advanced Features Admin Portal"
admin.site.index_title = "Welcome to Advanced Features Administration"
