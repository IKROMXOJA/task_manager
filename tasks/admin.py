from django.contrib import admin
from django.contrib.admin import AdminSite

class PremiumAdminSite(AdminSite):
    site_header = "⚡ Premium Admin Panel"
    site_title = "Calc Project Admin"
    index_title = "Boshqaruv markaziga xush kelibsiz"

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }

admin_site = PremiumAdminSite(name='premium_admin')
