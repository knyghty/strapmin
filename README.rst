Important
=========

This project is unmaintained. It was never a good solution to any problem, just better than
the alternatives I had at the time. If you think you want this - you don't.
Just use the stock admin.

If you really must have something that looks a little nicer, and does a bit more than stock,
try django-grapelli_ instead.

But I might be willing to keep this up to date in exchange for lots of money.

.. _django-grapelli: https://github.com/sehmaschine/django-grappelli

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
