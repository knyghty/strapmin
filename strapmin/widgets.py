from django import forms
from django.forms.util import flatatt
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


class RichTextEditorWidget(forms.Textarea):
    class Media:
        js = ('admin/js/ckeditor/ckeditor.js',
              'admin/js/ckeditor/jquery-ckeditor.js')

    def render(self, name, value, attrs={}):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(render_to_string('ckeditor/widget.html', {
            'final_attrs': flatatt(final_attrs),
            'value': force_text(value),
            'id': final_attrs['id'],
        }))
