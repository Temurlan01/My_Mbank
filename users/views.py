from django.shortcuts import render

from django.views.generic import TemplateView
from django.shortcuts import render


class ProfileListView(TemplateView):
    template_name = 'profile-page.html'

class AddMoneyListView(TemplateView):
    template_name = 'add-money-page.html'

class TransactionListView(TemplateView):
    template_name = 'transaction-page.html'

class LoginListView(TemplateView):
    template_name = 'login-page.html'

class RegisterListView(TemplateView):
    template_name = 'registration-page.html'
