from django.conf import settings
from django.contrib import admin
from django.urls import path
from users.views import ProfileListView, AddMoneyListView, TransactionListView, LoginListView, RegisterListView, \
    ClickButtonView, MakeRegistrationView, MakeTransactionView, MakeLogoutView, MakeLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', ProfileListView.as_view(), name='profile-url'),
    path('transactions-list/', TransactionListView.as_view(), name='transactions-url'),
    path('make-transfers/', MakeTransactionView.as_view(), name='make-transfers-url'),
    path('add-money-list/', AddMoneyListView.as_view(), name='mining-money-url'),
    path('add-money/', ClickButtonView.as_view(), name='add-money-url'),
    path('login-list/', LoginListView.as_view(), name='login-url'),
    path('make-login/', MakeLoginView.as_view(), name='make-login-url'),
    path('make-logaut/', MakeLogoutView.as_view(), name='logout-url'),
    path('register-list/', RegisterListView.as_view(), name='register-url'),
    path('make-registration/', MakeRegistrationView.as_view(), name='make-register-url')


]
