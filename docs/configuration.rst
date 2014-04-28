=============
Configuration
=============

.. contents::
   :depth: 2

-----------
settings.py
-----------
Open ``settings.py`` and add ``twentytab-customadmin`` to your ``INSTALLED_APPS`` (before django.contrib.admin)::

    INSTALLED_APPS = {
        ...,
        'customadmin',
        'django.contrib.admin',
        'inspectmodel',
        'imagekit',
        'image_ui',
        'rosetta',
        ...
    }

-------
urls.py
-------
Open ``urls.py`` and add those views to your ``urlpatters``::

    urlpatterns = patterns('',
        ... ,
        (r'^admin/', include(contrib.admin.site.urls)),
        (r'', include('customadmin.urls')),
        (r'^rosetta/', include('rosetta.urls')),
        (r'', include('inspectmodel.urls')),
        ...
    )

------------
Static files
------------
Run `collectstatic command`_ or map static directory. If you use `uWSGI`_ you can map static files::

    static-map = /static/customadmin/=%(path-to-site-packages)/customadmin/static/customadmin
    static-map = /static/colorful/=%(path-to-site-packages)/colorful/static/colorful
    static-map = /static/sortable/=%(path-to-site-packages)/sortable/static/sortable
    static-map = /static/image_ui/=%(path-to-site-packages)/image_ui/static/image_ui

.. _`collectstatic command`: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#collectstatic
.. _`uWSGI`: https://github.com/unbit/uwsgi


----------
Run syncdb
----------
Last (but not least) run::

    python manage.py syncdb

To create ``twentytab-customadmin`` tables, now your are ready for the funny part.
