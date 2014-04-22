from django import forms


class RichTextEditorWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'ckeditor'}
        super(RichTextEditorWidget, self).__init__(*args, **kwargs)

    class Media:
        js = ('admin/js/ckeditor/ckeditor.js',)
