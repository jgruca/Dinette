from django.forms import ModelForm
from django import forms

from django.conf import settings

from dinette.models import Ftopics ,Reply

#create a form from this Ftopics and use this when posting the a Topic
class FtopicForm(ModelForm):
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
    message = forms.CharField(widget = forms.Textarea(attrs={"cols":90, "rows":10}))
    class Meta:
        model = Reply
        if getattr(settings, 'DINETTE_DISABLE_UPLOADS', False):
            fields = ('message', 'message_markup_type')
        else:
            fields = ('message', 'message_markup_type', 'file')

