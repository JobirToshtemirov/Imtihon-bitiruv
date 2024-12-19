from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from app_users.models import UserModel


class TotalUsersAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_users = UserModel.objects.exclude(role='user').count()
        return Response({"total_users": total_users})
