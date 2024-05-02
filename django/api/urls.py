from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import PriceListViewSet, CalcListViewSet, CalcSquareListViewSet, PostListViewSet, PricesForCalc

urlpatterns = [
    path('prices-for-calc/', PricesForCalc.as_view(), name="prices_for_calc"),
]

router = SimpleRouter()
# router.register("users", UserViewSet, basename="users")

router.register("posts", PostListViewSet, basename="posts")
router.register("prices", PriceListViewSet, basename="prices")
router.register("calc-square", CalcSquareListViewSet, basename="calc_square")
router.register("calcs", CalcListViewSet, basename='calcs')

urlpatterns += router.urls
