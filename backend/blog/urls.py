from django.urls import path, include

from . import views


urlpatterns = [
    path('blog/', include([
        path('', views.BlogListView.as_view(), name='blog-list'),
        path('<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
        path('new/', views.PostCreateView.as_view(), name='new_post'),
        path('new/', views.PostEditView.as_view(), name='post_edit')
    ])),
]
