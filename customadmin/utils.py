from django.contrib import admin


def list_apps():

    apps = []
    for model, model_admin in admin.site._registry.items():
        app_label = model._meta.app_label

        apps.append(app_label)

    apps = [(a, a) for a in sorted(set(apps))]
    return apps


def list_models():

    apps = {}
    for model, model_admin in admin.site._registry.items():
        app_label = model._meta.app_label
        if app_label in apps.keys():
            apps[app_label].append((model.__name__, model.__name__))
        else:
            apps[app_label] = [(model.__name__, model.__name__)]

    res = []
    for app in sorted(apps.keys()):
        models_tuple = []
        for model in sorted(apps[app]):
            models_tuple.append(model)
        res.append((app, models_tuple))

    return res