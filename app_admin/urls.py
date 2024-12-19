from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, CourierViewSet
from .statistics.restourant import TotalRestaurantsAPIView
from .statistics.courier import TotalCouriersAPIView
from .statistics.branch import TotalBranchesAPIView
from .statistics.user import TotalUsersAPIView
from .statistics.order import OrdersStatisticsAPIView

router = DefaultRouter()
router.register('managers', ManagerViewSet)
router.register('couriers', CourierViewSet, basename="co")

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/restaurants/', TotalRestaurantsAPIView.as_view(), name='total-restaurants'),
    path('statistics/branches/', TotalBranchesAPIView.as_view(), name='total-branches'),
    path('statistics/users/', TotalUsersAPIView.as_view(), name='total-users'),
    path('statistics/couriers/', TotalCouriersAPIView.as_view(), name='total-couriers'),
    path('statistics/orders/', OrdersStatisticsAPIView.as_view(), name='orders-statistics'),
]

