from django.urls import path, include
from rest_framework import routers
from .views import *



router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'order', OrderViewSet, basename='order'),
router.register(r'review', ReviewViewSet, basename='review'),
router.register(r'cart', CartViewSet, basename='cart'),
router.register(r'cart_item', CartItemViewSet, basename='cart_item'),


urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('store/create/', StoreCreateAPIView.as_view(), name='store_create'),
    path('combo/', ComboListAPIView.as_view(), name='combo_list'),
    path('combo/<int:pk>', ComboDetailAPIView.as_view(), name='combo_detail'),
    path('combo/create/', ComboCreateAPIView.as_view(), name='combo_create'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),

]