strapmin
========

strapmin is a reskin of the django admin using Twitter Bootstrap.

It's fully responsive and includes CKEditor for easy editing of HTML.


Installation
------------

1. `pip install strapmin`
2. Add request to your context processors::

        from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
        TEMPLATE_CONTEXT_PROCESSORS = TCP + ('django.core.context_processors.request',)

3. Add 'strapmin' to your INSTALLED_APPS::

        INSTALLED_APPS = (
            'strapmin',
            'django.contrib.admin',
            ...
        )

Note: You must add `strapmin` *before* `django.contrib.admin`



Usage
-----

Create your `ModelAdmin` classes as normal.


CKEditor
~~~~~~~~

To include a CKEditor instance for all TextFields in a model::

    from django.contrib import admin
    from django.db import models

    from strapmin.widgets import RichTextEditorWidget

    from polls.models import Poll


    class ArticleAdmin(admin.ModelAdmin):
        formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}

For a subset of models, make a form for your model that uses the widget::

    from django import forms

    from strapmin.widgets import RichTextEditorWidget

    from polls.models import Poll


    class PollForm(forms.ModelForm):
        class Meta:
            model = Poll
            widgets = {'content': RichTextEditorWidget}


License
-------

strapmin is licensed under a BSD 2-Clause License.
