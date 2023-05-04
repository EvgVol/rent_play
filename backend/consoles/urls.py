from django.urls import path

from . import views


urlpatterns = [
    path('consoles/', views.ConsoleView.as_view(), name='consoles'),
    path('consoles/list/', views.ConsoleListView.as_view(), name='console_list'),
    path('consoles/1/', views.ConsoleDetailView.as_view(), name='console_detail'),
    path('consoles/cart/', views.ConsoleCartView.as_view(), name='cart'),
    path('consoles/checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('consoles/new/', views.NewConsoleView.as_view(), name='new_console'),
]
