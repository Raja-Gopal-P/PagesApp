from django.contrib import admin
from .models import Page
from django.urls import path
from .views import reorder_page


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        custom_urls = [
            path(r'reorder/', self.admin_view(reorder_page), name="reorder"),
        ]
        return custom_urls


custom_admin = CustomAdminSite(name='my_admin')

admin.site.register(Page)
