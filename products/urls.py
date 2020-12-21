from django.urls import path
from .views import product_create_list_view, product_add_list_view, ProductUpdateView, ProductSellView, ProductBuyView, product_post_buy, ProductCancelView


app_name = 'products'

urlpatterns =[
    path('', product_create_list_view, name='main-product-view'),
    path('add/', product_add_list_view, name='product-add-view'),
    path('<pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<pk>/sell/', ProductSellView.as_view(), name='product-sell'),
    path('<pk>/buy/', ProductBuyView.as_view(), name='product-buy'),
    path('success/', product_post_buy, name='product-buy-success'),
    path('<pk>/cancel/', ProductCancelView.as_view(), name='product-cancel'),
]