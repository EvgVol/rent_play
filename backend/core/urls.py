from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('work/', views.work, name='work'),
    path('work-detail/', views.work_detail, name='work_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/1/', views.post, name='sing_post'),
    
    # path('sections/<int:num>', views.section, name='section'),
    # path('consoles/', views.consoles, name='consoles'),
    # path('consoles/1/', views.console_id, name='console_id'),
    # path('games/', views.games, name='games'),
    # path('games/1/', views.game_id, name='game_id'),
    # path('blog/', views.blog, name='blog'),
]
