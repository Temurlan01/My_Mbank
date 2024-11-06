from django.shortcuts import render

from django.views.generic import TemplateView

from users.models import CustomUser


class ProfileListView(TemplateView):
    template_name = 'profile-page.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = {
            'current_user': current_user
        }
        return context

class AddMoneyListView(TemplateView):
    template_name = 'add-money-page.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = {
            'current_user': current_user
        }
        return context


class ClickButtonView(TemplateView):
    template_name = 'add-money-page.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        current_user.balance += 1
        current_user.save()
        context = {
            'current_user': current_user
        }
        return context

class TransactionListView(TemplateView):
    template_name = 'transaction-page.html'

class LoginListView(TemplateView):
    template_name = 'login-page.html'

class RegisterListView(TemplateView):
    template_name = 'registration-page.html'
