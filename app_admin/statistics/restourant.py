from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from app_company.models import RestaurantModel


class TotalRestaurantsAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_restaurants = RestaurantModel.objects.count()
        return Response({"total_restaurants": total_restaurants})
