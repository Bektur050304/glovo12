from gc import get_count

from rest_framework import serializers
from .models import *



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['comment', 'rating']


class StoreListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'description', 'category', 'avg_rating', 'count_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'



class CategoryDetailSerializer(serializers.ModelSerializer):
    category = StoreListSerializer

    class Meta:
        model = Category
        fields = ['category_name']



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'price']


class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'image', 'price']



class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'image', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSimpleSerializer

    class Meta:
        model = CartItem
        fields = ['product']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'



class ComboListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['combo_name', 'description', 'combo_image']



class ComboDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['combo_name', 'description', 'price', 'combo_image']




class StoreDetailSerializer(serializers.ModelSerializer):
    store_product = ProductSimpleSerializer(many=True,read_only=True)
    combo_for_store = ComboListSerializer(many=True,read_only=True)
    store_review = ReviewSimpleSerializer(many=True)


    class Meta:
        model = Store
        fields = ['store_name', 'store_image', 'store_product','combo_for_store', 'store_review']



