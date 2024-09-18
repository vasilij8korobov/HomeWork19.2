# from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contacts/', contacts, name='home')
]
