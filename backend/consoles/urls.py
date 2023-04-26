from django.urls import path

from . import views


urlpatterns = [
    path('/', views.ConsoleView.as_view(), name='consoles'),
    path('/list/', views.ConsoleListView.as_view(), name='console_list'),
    path('/1/', views.ConsoleDetailView.as_view(), name='console_detail'),
    path('/cart/', views.ConsoleCartView.as_view(), name='cart'),
    path('/checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('/new/', views.NewConsoleView.as_view(), name='new_console'),
]
