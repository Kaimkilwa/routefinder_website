from django import forms
from .models import JobseekersPersonalIfor, JobseekersJobinfor
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget

GENDER = {
    ('M', 'Male'),
    ('F', 'Female'),
}
LOCATION = {
    ('M', 'MWANZA'),
    ('K', 'KAGERA'),
}
NATIONALITY = {

    ('AL', 'Algeria'),
    ('AN', 'Angola'),
}
YEARS = [x for x in range(1940, 2021)]


class JobForm(forms.ModelForm):
    birthday = forms.DateField(label='What is your birth date?',
                               initial="1990-06-21",
                               widget=forms.SelectDateWidget(attrs={
                                   'style': ' width:;',
                                   'class': 'form-control',
                                   'placeholder': 'Write your birth date'}, years=YEARS))
    email = forms.EmailField(max_length=30,
                             widget=forms.EmailInput(attrs={
                                 'style': ' width:;',
                                 'placeholder': 'Write your email here'
                             }))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'style': ' width:; ',
                                   'placeholder': 'Write your password here'
                               }))
    firstname = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={
                                    'style': ' width:;',
                                    'placeholder': 'Write your name here'
                                }))
    lastname = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'style': ' width:;',
            'placeholder': 'Write your lastname here'}))
    phone_number = forms.CharField(label=_("Phone"), max_length=200,
                                   widget=forms.TextInput(attrs={
                                       'style': ' width:',
                                       'class': 'form-control',
                                       'placeholder': 'Eg: +255.........'}))

    class Meta:
        model = JobseekersPersonalIfor
        fields = (
        'email', 'password', 'firstname', 'middlname', 'lastname', 'birthday', 'gender', 'location', 'phone_number',
        'nationality')


# this form for job information
class JobinfoForm(forms.ModelForm):
    receive_job_notifation = forms.BooleanField(label='Would you like to receive Job notifications?', initial=True)

    class Meta:
        model = JobseekersJobinfor
        fields = ('personalinfo', 'highest_qualification', 'years_of_exprience', 'cv', 'receive_job_notifation')
