from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'DjangoBlog0607.myadmin.MyAdminSite'
