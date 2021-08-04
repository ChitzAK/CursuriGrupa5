import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import UpdateView, CreateView

from userprofile.forms import NewAccountForm
from userprofile.models import UserExtend


class UpdateProfile(LoginRequiredMixin, UpdateView):
    # fields = ['first_name', 'last_name', 'email']
    form_class = NewAccountForm
    model = User
    template_name = 'registration/new_account.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs

    def form_valid(self, form):
        if form.is_valid() and form.errors is False:
            form.save(commit=False)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('aplicatie1:listare')


punctuation = '!$%?#@'


class CreateNewAccount(LoginRequiredMixin, CreateView):
    form_class = NewAccountForm
    model = UserExtend
    template_name = 'registration/new_account.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'pk': None})
        return kwargs

    def form_valid(self, form):
        if form.is_valid() and form.errors is False:
            form.save(commit=False)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +
                                                   punctuation) for _ in range(8))
        try:
            user_instance = User.objects.get(id=self.object.id)
            user_instance.set_password(psw)
            user_instance.save()
            content_email_user = f"Your username and password: {user_instance.username} {psw}"
            msg_html = render_to_string('registration/invite_user.html', {"content_email": content_email_user})
            email = EmailMultiAlternatives(subject='Invite user', body=content_email_user, from_email='contact@test.ro',
                                           to=[user_instance.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        except Exception:
            pass
        return reverse('aplicatie1:listare')
