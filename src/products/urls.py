from django.urls import path

from .views import (
    product_detail_view,
    product_create_view,
    dynamic_lookup_view,
    product_delete_view
    )


# unique variable name in urls file
app_name = 'product_detail'

urlpatterns = [
    # passing parameter to perform GET method
    path('', product_detail_view, name='product-detail-all'),
    path('<int:my_id>/', product_detail_view, name='product-detail-id'),
    path('<int:my_id>/delete/', product_delete_view, name='product-delete-id'),
    path('create/', product_create_view, name='product-detail-create'),
]
