========
Tutorial
========

In your admin interface you now have ``Customadmin`` app with 4 models:

.. contents::

.. _Custom Admin:

------------
Custom Admin
------------
As the name suggests this model is the core of this app, here you can customize the general aspect of the admin interface.

Branding
........

**Branding**: Set Branding. (default: Django Administration)

**Branding link**: Set Branding's link. (ex. '/' to redirect to the homepage) (default: No redirect)

**Branding image**: Set a logo to be displayed with or instead of the Branding. (default: No image)

**Default**: Set it if you want to enable this Custom Admin configuration.

View Option
...........

**View mode**:  This is the most important option. Set the interface that you prefer between 5 options:

    *------------*: Keep the default django admin interface with the options that you set in this configuration but you cannot use :ref:`Custom App`, :ref:`Custom Model` and :ref:`Custom Link`.

    *Use custom app system*:    Like *------------* but you can use :ref:`Custom App`, :ref:`Custom Model` and :ref:`Custom Link`.

    *Use apps' icon system*:    Apps in the admin homepage are shown as icons intead of a list of links to models.

    *Use apps and models icon system*:  Like *Use apps' icon system* but models too are shown as icons instead of a list of links.

    *Use models' icons system in index group models by app*:    Models are shown as icons grouped by app in the admin homepage.

    *Use models' icons system in index ungroup models by app*:  Like *Use models' icons system in index group models by app* but models are not grouped by app.

**Use log sidebar**: Check if you want the log sidebar in the admin homepage to be shown.

**Autocomplete app**: Uncheck if you want ``customadmin`` to hide the apps not defined in :ref:`Custom App`.

**Autocomplete model**: Uncheck if you want ``customadmin`` to hide the apps not defined in :ref:`Custom Model`.

Images
......

**Default app image**: Set an image that will replace the default app icon shown in the admin homepage. (this image will be applied to all apps, you can set different images per app in :ref:`Custom App`)

**Default model image**: Set an image that will replace the default model icon shown in the admin homepage. (this image will be applied to all models, you can set different images per model in :ref:`Custom Model`)

Style
.....
Here you can change colors, font, font-size and so on to the admin interface. (default: if not changed it keeps django administration default style)

Code
....
**Html head**: Add extra code to the <head> tag. (ex. you can add some javascript)

**Css code**: Add extra css.

**Use css code**: if not checked the css code defined in **Css code** is disabled.

.. _Custom Model:

------------
Custom Model
------------

.. _Custom App:

----------
Custom App
----------

.. _Custom Link:

-----------
Custom Link
-----------
