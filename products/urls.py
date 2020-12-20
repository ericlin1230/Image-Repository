from django.urls import path
from .views import product_create_list_view, product_add_list_view, ProductUpdateView


app_name = 'products'

urlpatterns =[
    path('', product_create_list_view, name='main-product-view'),
    path('add/', product_add_list_view, name='product-add-view'),
    path('<pk>/update/', ProductUpdateView.as_view(), name='product-update'),
]