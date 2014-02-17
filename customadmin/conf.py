from appconf import AppConf
from django.conf import settings


class CustomAdminConf(AppConf):
    STATIC_URL = u'/static/'
    USE_CUSTOM_ADMIN = True

    def configure_static_url(self, value):
        if not getattr(settings, 'STATIC_URL', None):
            self._meta.holder.STATIC_URL = value
            return value
        return getattr(settings, 'STATIC_URL')

    def configure_use_custom_admin(self, value):
        if not getattr(settings, 'USE_CUSTOM_ADMIN', None):
            self._meta.holder.USE_CUSTOM_ADMIN = value
            return value
        return getattr(settings, 'USE_CUSTOM_ADMIN')

    def configure(self):
        if self.configured_data['USE_CUSTOM_ADMIN']:
            from django.contrib.admin.sites import site

            site.index_template = "admin/custom_index.html"
            site.app_index_template = "admin/app_index.html"

        if not getattr(settings, 'TEMPLATE_CONTEXT_PROCESSORS', None):
            self._meta.holder.TEMPLATE_CONTEXT_PROCESSORS = [
                'customadmin.template_context.context_processors.customadmin_context'
            ]
        else:
            middleware = getattr(settings, 'TEMPLATE_CONTEXT_PROCESSORS')
            middleware.append('customadmin.template_context.context_processors.customadmin_context')
            self._meta.holder.TEMPLATE_CONTEXT_PROCESSORS = middleware

        return self.configured_data