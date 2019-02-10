from django.contrib import admin
from django.urls import path, include

from shipments import views as shipments_views
from companies import views as companies_views
from products import views as products_views

api_urls = ([
    path('shipments', shipments_views.ShipmentsAPIView.as_view(), name='shipments'),
], 'v1')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
]
