from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    """GET /api/v1/order/ list orders, POST create an order."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE /api/v1/order/{id} for a single order."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserOrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE /api/v1/user/{id}/order/{id}"""
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id' 

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Order.objects.filter(user_id=user_id)