from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ExportMixin
from import_export import resources



# Register your models here.



class UserResource(resources.ModelResource):
    class Meta:
        search_fields =('id','first_name','last_name',)
        model = User
        fields = ('username','first_name', 'last_name', 'email','is_staff','is_active','is_superuser')
        export_order = ('username','first_name', 'last_name', 'email','is_staff','is_active','is_superuser')

class UserAdmin(ExportMixin, UserAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin )
