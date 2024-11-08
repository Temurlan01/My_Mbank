from django.conf import settings
from django.contrib import admin
from django.urls import path
from users.views import ProfileListView, AddMoneyListView, TransactionListView, LoginListView, RegisterListView, \
    ClickButtonView, MakeRegistrationView, MakeTransactionView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('profile/', ProfileListView.as_view(), name='profile-url'),

    path('add-money/', AddMoneyListView.as_view(), name='add-money'),
    path('click-button/', ClickButtonView.as_view(), name='click-button-url'),

    path('transaction/', TransactionListView.as_view(), name='transactions'),
    path('make-transaktion/', MakeTransactionView.as_view(), name='make-transaction-url'),

    path('login/', LoginListView.as_view(), name='login'),

    path('register/', RegisterListView.as_view(), name='register-url'),
    path('registration', MakeRegistrationView.as_view(), name='registration-url'),


]
