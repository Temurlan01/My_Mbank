from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError, transaction
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from users.models import CustomUser
from django.views import View
import requests


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
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('profile-url')
        else:
            return redirect('login-url')


class RegisterListView(TemplateView):
    template_name = 'registration-page.html'


class ProfileListView(TemplateView):
    template_name = 'profile-page.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user

        API_KEY = "ae5ad3d6b43e7671c758b11d"
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/KGS"
        response = requests.get(url)
        data = response.json()
        currencies = data['conversion_rates']
        USD = currencies['USD']
        user_dollar_balance = USD * current_user.balance

        context = {
            'current_user': current_user,
            'dollar_balance': round(user_dollar_balance, 1)

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

    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        current_user.balance += 100
        current_user.save()
        context = {'current_user': current_user}

        return render(request, self.template_name, context)


class MakeTransactionView(TemplateView):

    def post(self, request, *args, **kwargs):

        input_data = request.POST
        phone_number = input_data['phone']
        amount = int(input_data['amount'])
        sender = request.user

        try:
            receiver = CustomUser.objects.get(phone_number=phone_number)
        except:
            return  HttpResponse('Такого номера не существует')

        if sender.balance < amount:
            return HttpResponse('У вас недостаточно средств!')

        if sender.phone_number == phone_number:
            return HttpResponse ('Нельзя отправлять самому себе ')

        if amount > sender.balance or amount <= 0:
            return HttpResponse('Вы пытаетесь отправить отрицательное число или у вас недостаточно средств на балансе')


        with transaction.atomic():  # атомарная транзакция в бд
            receiver.balance += amount
            sender.balance -= amount

            receiver.save()
            sender.save()

        return redirect('profile-url')

class SnakeListView(TemplateView):
    template_name = 'snake.html'


