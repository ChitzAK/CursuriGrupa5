from django import forms
from django.contrib.auth.models import User

from userprofile.models import UserExtend


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'username', 'company']

    def __init__(self, pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        print(self.pk, '>>>>')
        if self.pk is not None:
            if User.objects.filter(email=email_value).exclude(id=self.pk).exists():
                msg = 'Emailul deja exista, te rugam sa adaugi un email unic'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_value).exclude(id=self.pk).exists():
                msg = 'Username-ul deja exista, te rugam sa adaugi un username unic'
                self._errors['username'] = self.error_class([msg])
        else:
            if User.objects.filter(email=email_value).exists():
                msg = 'Emailul deja exista, te rugam sa adaugi un email unic'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_value).exists():
                msg = 'Username-ul deja exista, te rugam sa adaugi un username unic'
                self._errors['username'] = self.error_class([msg])
        return field_data
