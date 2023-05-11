from django.urls import path, include

from . import views


urlpatterns = [
    path('blog/', include([
        path('', views.BlogListView.as_view(), name='blog-list'),
        path('<int:pk>/', include([
            path('', views.BlogDetailView.as_view(), name='blog-detail'),
            path('edit/', views.PostEditView.as_view(), name='post_edit'),
            path('delete/', views.PostDeleteView.as_view(), name='post_delete'),
        ])),
        path('new/', views.PostCreateView.as_view(), name='new_post'),
    ])),
]
