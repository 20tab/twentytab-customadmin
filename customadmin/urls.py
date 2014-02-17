"""
It defines the urlpattern for css file with rules for admin's interface customization.
"""
from django.conf.urls import *
urlpatterns = patterns('',
        (r'^custom_admin_layout.css$', 'customadmin.views.custom_admin_layout'),
)
