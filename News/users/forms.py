from django import forms
from .validators import russian_email
from django.core.validators import MinLengthValidator
from django.forms import TextInput, EmailInput, FileInput, Select
from .models import Account

class AccountUpdateForm(forms.Form):
    class Meta:
        model = Account
        fields = ['phone', 'address', 'vk', 'instagram', 'telegram', 'account_image']
        widgets = {'phone': TextInput({'class': 'textinput form-control',
                                       'placeholder': 'phone number'}),
                   'address': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'address'}),
                   'vk': TextInput({'class': 'textinput form-control',
                                      'placeholder': 'vk'}),
                   'instagram': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'instagram'}),
                   'telegram': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'telegram'}),
                   'account_image': FileInput({'class': 'form-control',
                                       'placeholder': 'image'})
                   }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           validators=[MinLengthValidator(2)],
                           initial='Имя')
    email = forms.EmailField(validators=[russian_email])
    message = forms.CharField(widget=forms.TextInput, disabled=True)
    demo = forms.BooleanField(required=False,
                              help_text='Текст-подсказка',
                              label='Вам нравится?',
                              initial=True)