from django.contrib import admin
from .models import myUser,Temp_Token



class admin_user(admin.ModelAdmin):
    class Meta:
        model = myUser


    list_display = ['username','phone_number','is_active']
    list_editable = ['is_active']
    sortable_by = ['is_active','is_superuser']
    search_fields = ['username']
    list_filter = ['is_active','is_staff']


admin.site.register(myUser, admin_user)
admin.site.register(Temp_Token)