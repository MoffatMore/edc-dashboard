from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Example'
    site_header = 'Example'
    index_title = 'Example'
    site_url = '/'


edc_dashboard_admin = AdminSite(name='edc_dashboard_admin')
