from django import template
from django.contrib import admin
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils import six
from django.utils.text import capfirst

try:
    from django.apps import apps
    has_appconfig = True
except:
    has_appconfig = False

register = template.Library()
site = admin.site


@register.assignment_tag(takes_context=True)
def get_app_list(context):
    request = context['request']
    app_dict = {}
    user = request.user
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        if has_appconfig:
            app_name = apps.get_app_config(app_label).verbose_name
        has_module_perms = user.has_module_perms(app_label)

        if has_module_perms:
            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True in perms.values():
                info = (app_label, model._meta.module_name)
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'perms': perms,
                }
                if has_appconfig:
                    model_dict['object_name'] = model._meta.object_name

                if perms.get('change', False):
                    try:
                        model_dict['admin_url'] = reverse(
                            'admin:%s_%s_changelist' % info)
                    except NoReverseMatch:
                        pass
                if perms.get('add', False):
                    try:
                        model_dict['add_url'] = reverse(
                            'admin:%s_%s_add' % info)
                    except NoReverseMatch:
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    if has_appconfig:
                        name = app_name
                    else:
                        name = app_label.title()

                    app_dict[app_label] = {
                        'name': name,
                        'app_label': app_label,
                        'app_url': reverse('admin:app_list',
                                           kwargs={'app_label': app_label},
                                           current_app=site.name),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    # Sort the apps alphabetically.
    app_list = list(six.itervalues(app_dict))
    app_list.sort(key=lambda x: x['name'])

    # Sort the models alphabetically within each app.
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])

    return app_list
