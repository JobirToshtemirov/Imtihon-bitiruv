from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from app_users.models import UserModel


class TotalCouriersAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_couriers = UserModel.objects.filter(role='courier').count()
        return Response({"total_couriers": total_couriers})
