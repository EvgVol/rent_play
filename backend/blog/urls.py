from django.urls import path, include

from . import views


urlpatterns = [
    path('blog/', include([
        path('', views.BlogListView.as_view(), name='blog-list'),
        path('<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail')
    ])),

    # path('/', views.blog, name='blog'),
    # path('/<int:post_id>/', views.post_detail, name='post_detail'),
]
