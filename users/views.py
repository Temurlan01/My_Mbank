from django.http import Http404
from django.shortcuts import render, redirect
from django.db import IntegrityError, transaction
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from users.models import CustomUser
from django.contrib import messages
from django.views import View


class LoginListView(TemplateView):
    template_name = 'login-page.html'


class MakeLoginView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        phone_number = data.get('phone')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            messages.error(request, "Пользователь с таким номером телефона не найден.")
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('profile-url')
        else:
            messages.error(request, "Неверный пароль.")
            return redirect('login-url')


class RegisterListView(TemplateView):
    template_name = 'registration-page.html'


class ProfileListView(TemplateView):
    template_name = 'profile-page.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = {
            'current_user': current_user
        }
        return context


class TransactionListView(TemplateView):
    template_name = 'transaction-page.html'


class MakeLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login-page.html', {})


class MakeRegistrationView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        password = data['password']
        phone_number = data['phone']
        username = data['name']

        try:
            user = CustomUser.objects.create_user(
                first_name=username,
                password=password,
                phone_number=phone_number
            )
            user.save()

            login(request, user)
            return redirect('profile-url')
        except IntegrityError:
            messages.error(request, "Такой номер телефона уже зарегистрирован.")
            return redirect('register-url')


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
        current_user.balance += 1000
        current_user.save()
        context = {
            'current_user': current_user
        }
        return context


class MakeTransactionView(TemplateView):

    def post(self, request, *args, **kwargs):

        input_data = request.POST
        phone_number = input_data['phone']
        amount = int(input_data['amount'])
        sender = request.user

        try:
            receiver = CustomUser.objects.get(phone_number=phone_number)
        except:
            raise Http404

        if amount > sender.balance or amount <= 0:
            return redirect('transactions-url')

        with transaction.atomic():
            receiver.balance += amount
            sender.balance -= amount

            receiver.save()
            sender.save()

        return redirect('profile-url')




