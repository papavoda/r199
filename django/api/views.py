from rest_framework import generics, viewsets
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


from blog.models import Post
from price.models import Price
from .serializers import PriceListSerializer, CalcListSerializer, CalcSquareListSerializer, PostListSerializer
from calc.models import Calc, CalcSquare
from rest_framework.views import APIView

class CalcSquareListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = CalcSquare.objects.all()
    serializer_class = CalcSquareListSerializer


class CalcListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Calc.objects.all()
    serializer_class = CalcListSerializer


class PriceListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Price.objects.select_related('category').all()
    serializer_class = PriceListSerializer



class PostListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Post.objects.select_related('category', 'author').filter(status='published').order_by('-pub_at')
    serializer_class = PostListSerializer

    """
        "List view"
        self.basename from urls.py  router.register("news", PostListViewSet, basename="news")
    """

class PricesForCalc(APIView):
    prices = Price.objects.select_related('category').filter(use_in_calc=True)
    serializer = PriceListSerializer(prices, many=True)

    # Cache page for the requested url
    # @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        return Response(self.serializer.data)
