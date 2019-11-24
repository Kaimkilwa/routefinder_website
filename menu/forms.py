from django import forms 
from .models import ContactModel
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.ModelForm):
 
  customername = forms.CharField(label=_("Your name"),max_length=200,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Enter your name........'}))
  customeremail = forms.CharField(label=_("Email"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'example@gmail.xom'}))
  subject = forms.CharField(max_length=200,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Enter subject......'}))
  massege = forms.CharField(max_length=200,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Enter yor comment here......'}))
  class Meta:
    model = ContactModel
    fields = ('customername','customeremail', 'subject' ,'massege')
