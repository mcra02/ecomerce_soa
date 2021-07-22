from django.urls import path

from apps.Products.api.views.general_views import MeasureUnitListAPIView
#from apps.Products.api.views.product_views import ProductListAPIView,ProductCreateAPIView,ProductRetrieveAPIView,ProductDestroyAPIView,ProductUpdateAPIView

urlpatterns = [
    '''
    path('measure_unit/',MeasureUnitListAPIView.as_view(), name ='measure_unit'),
    path('product/list',ProductListAPIView.as_view(), name ='product'),
    path('product/create',ProductCreateAPIView.as_view(), name ='product_create'),
    path('product/retrieve/<int:pk>',ProductRetrieveAPIView.as_view(), name ='product_retrieve'),
    path('product/destroy/<int:pk>',ProductDestroyAPIView.as_view(), name ='product_destroy'),
    path('product/update/<int:pk>',ProductUpdateAPIView.as_view(), name ='product_update'),
    '''
]
