from rest_framework import serializers, request
from rest_framework.fields import SerializerMethodField
from rest_framework.reverse import reverse_lazy

# from blog.models import Post
from price.models import Price
from calc.models import Calc, CalcSquare


class CalcSquareListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalcSquare
        fields = '__all__'


class CalcListSerializer(serializers.ModelSerializer):
    # price = SerializerMethodField('get_price')
    # def get_price(self, instance):
    #     if instance.price:
    #         return instance.price.price
    # square_fields = CalcSquareListSerializer(many=True, read_only=True)
    price = serializers.ReadOnlyField(source='price.price')
    name = serializers.ReadOnlyField(source='price.name')
    price_category = serializers.ReadOnlyField(source='price.category.id')
    price_category_name = serializers.ReadOnlyField(source='price.category.name')

    class Meta:
        model = Calc
        fields = ('id', 'name', 'price_category', 'price_category_name', 'material', 'price', 'amount',
                  'unit', 'dimension', 'thickness', 'boxing', )
        # fields = '__all__'


class PriceListSerializer(serializers.ModelSerializer):
    category_name = SerializerMethodField('get_category_name')

    def get_category_name(self, instance):
        if instance.category:
            return instance.category.name

    class Meta:
        model = Price
        fields = ('id', 'category', 'category_name', 'name', 'price', 'dimension')

# class PostListSerializer(serializers.ModelSerializer):
#     main_image_url = SerializerMethodField('get_main_image')
#     post_url = SerializerMethodField('get_post_absolute_url')
#
#     def get_main_image(self, instance):
#         if instance.main_image:
#             return instance.main_image.url
#
#     def get_post_absolute_url(self, instance):
#         if instance:
#             return instance.get_absolute_url()
#
#     ### TODO make main_image as url in list view
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'post_url', 'intro', 'main_image', 'main_image_url')
