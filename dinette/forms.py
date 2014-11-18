from django.forms import ModelForm
from django import forms

from django.conf import settings

from dinette.models import Ftopics ,Reply

#create a form from this Ftopics and use this when posting the a Topic
class FtopicForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FtopicForm, self).__init__(*args, **kwargs)
        default_markup_type = getattr(settings, 'DEFAULT_MARKUP_TYPE', None)
        if default_markup_type:
            self.fields['message_markup_type'] = forms.CharField(
                widget=forms.HiddenInput, initial=default_markup_type
            )

    subject = forms.CharField(widget = forms.TextInput(attrs={"size":90}))
    message = forms.CharField(widget = forms.Textarea(attrs={"cols":90, "rows":10}))

    class Meta:
        model = Ftopics
        if getattr(settings, 'DINETTE_DISABLE_UPLOADS', False):
            fields = ('subject', 'message', 'message_markup_type')
        else:
            fields = ('subject', 'message', 'message_markup_type', 'file')


#create a form from Reply
class ReplyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        default_markup_type = getattr(settings, 'DEFAULT_MARKUP_TYPE', None)
        if default_markup_type:
            self.fields['message_markup_type'] = forms.CharField(
                widget=forms.HiddenInput, initial=default_markup_type
            )

    message = forms.CharField(widget = forms.Textarea(attrs={"cols":90, "rows":10}))

    class Meta:
        model = Reply
        if getattr(settings, 'DINETTE_DISABLE_UPLOADS', False):
            fields = ('message', 'message_markup_type')
        else:
            fields = ('message', 'message_markup_type', 'file')

