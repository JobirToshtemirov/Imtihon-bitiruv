from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from app_company.models import RestaurantModel
from app_branch.models import BranchModel


class TotalBranchesAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_branches = BranchModel.objects.count()

        restaurants_data = []
        restaurants = RestaurantModel.objects.all()

        for restaurant in restaurants:
            branches = BranchModel.objects.filter(restaurant=restaurant)
            branch_names = [branch.name for branch in branches]
            restaurants_data.append({
                "restaurant_name": restaurant.name,
                "total_branches": branches.count(),
                "branches": branch_names,
            })

        return Response({
            "total_branches": total_branches,
            "restaurants": restaurants_data,
        })
