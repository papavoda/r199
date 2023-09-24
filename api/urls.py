from rest_framework.routers import SimpleRouter

from .views import PriceListViewSet, CalcListViewSet, CalcSquareListViewSet

router = SimpleRouter()
# router.register("users", UserViewSet, basename="users")


router.register("prices", PriceListViewSet, basename="prices")
router.register("calc-square", CalcSquareListViewSet, basename="calc_square")
router.register("calcs", CalcListViewSet, basename='calcs')
urlpatterns = router.urls
