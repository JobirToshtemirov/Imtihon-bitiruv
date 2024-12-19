from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from app_deliveries.models import OrderModel


class OrdersStatisticsAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        today = datetime.now().date()
        month_start = datetime(today.year, today.month, 1)
        year_start = datetime(today.year, 1, 1)

        Orders_today = OrderModel.objects.filter(created_at__date=today).count()
        Orders_month = OrderModel.objects.filter(created_at__gte=month_start).count()
        Orders_year = OrderModel.objects.filter(created_at__gte=year_start).count()

        return Response({
            "Orders_today": Orders_today,
            "Orders_month": Orders_month,
            "Orders_year": Orders_year,
        })
