from django.urls import path
from book.api_views import BookListCreateAPIView, BookDetailAPIView
from order.api_views import OrderListCreateAPIView, OrderDetailAPIView, UserOrderDetailAPIView

urlpatterns = [
    path('book/', BookListCreateAPIView.as_view(), name='api-book-list'),
    path('book/<int:pk>/', BookDetailAPIView.as_view(), name='api-book-detail'),

    path('order/', OrderListCreateAPIView.as_view(), name='api-order-list'),
    path('order/<int:pk>/', OrderDetailAPIView.as_view(), name='api-order-detail'),

    path('user/<int:user_id>/order/<int:order_id>/', UserOrderDetailAPIView.as_view(), name='api-user-order-detail'),
]