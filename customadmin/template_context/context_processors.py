from __future__ import unicode_literals
from customadmin.models import CustomAdmin, CustomLink
from django.conf import settings
import django


def customadmin_context(request):
    """
    This context processor adds to request context CustomAdmin default instance
    and all CustoLink to customize django's admin
    """
    context_extras = {}
    if request.path.startswith('/admin'):
        try:
            context_extras['CUSTOM_ADMIN'] = CustomAdmin.objects.select_related().get(default=True)
            context_extras['CUSTOM_LINK_LIST'] = CustomLink.objects.select_related().all()
            context_extras['CUSTOM_ADMIN_CSS_ICONS'] = True
        except CustomAdmin.DoesNotExist:
            context_extras['CUSTOM_ADMIN'] = None
            context_extras['CUSTOM_ADMIN_CSS_ICONS'] = False
        if settings.USE_CUSTOM_ADMIN is not None:
            context_extras['USE_CUSTOM_ADMIN'] = settings.USE_CUSTOM_ADMIN
        else:
            context_extras['USE_CUSTOM_ADMIN'] = False
        context_extras['django_version'] = int('{}{}'.format(django.VERSION[0], django.VERSION[1]))
    return context_extras
