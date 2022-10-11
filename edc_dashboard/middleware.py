from django.conf import settings
from edc_constants.constants import FEMALE, OTHER, YES, NO, NOT_APPLICABLE
from edc_constants.constants import NEW, OPEN, CLOSED


class DashboardMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.url_name_data
        except AttributeError:
            request.url_name_data = {}
        try:
            request.template_data
        except AttributeError:
            request.template_data = {}
        response = self.get_response(request)
        return response

    def process_view(self, request, *args):
        url_name_data = {}
        try:
            settings.DASHBOARD_URL_NAMES
        except AttributeError:
            pass
        else:
            url_name_data.update(**settings.DASHBOARD_URL_NAMES)
        try:
            template_data = settings.DASHBOARD_BASE_TEMPLATES
        except AttributeError:
            template_data = {}
        request.url_name_data.update(**url_name_data)
        request.template_data.update(**template_data)

    def process_template_response(self, request, response):
        try:
            response.context_data.update(**request.url_name_data)
            response.context_data.update(**request.template_data)
        except AttributeError:
            response.renderer_context.update(**request.url_name_data)
            response.renderer_context.update(**request.template_data)

        try:
            reviewer_site_id = settings.REVIEWER_SITE_ID
        except AttributeError:
            reviewer_site_id = None
        options = {
            'OPEN': OPEN,
            'CLOSED': CLOSED,
            'FEMALE': FEMALE,
            'NEW': NEW,
            'NO': NO,
            'NOT_APPLICABLE': NOT_APPLICABLE,
            'OTHER': OTHER,
            'YES': YES,
            'reviewer_site_id': reviewer_site_id,
            }
        try:
            response.context_data.update(**options)
        except AttributeError:
            response.renderer_context.update(**options)
        return response
