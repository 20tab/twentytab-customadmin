twentytab-customadmin
=====================

A django app to customize your admin interface with icons for applications and models and other stuffs

## Installation

Use the following command: <b><i>pip install twentytab-customadmin</i></b>

## Configuration

- settings.py

Open settings.py and add customadmin to your INSTALLED_APPS (before django.contrib.admin):

```py
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
```

- urls.py

```py
urlpatterns = patterns('',
    ... ,
    (r'^admin/', include(contrib.admin.site.urls)),
    (r'', include('customadmin.urls')),
    (r'^rosetta/', include('rosetta.urls')),
    (r'', include('inspectmodel.urls')),
    ...
)

```
