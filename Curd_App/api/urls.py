from django.conf.urls import url , include
from Curd_App.api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp',views.ProductDataView)

urlpatterns = [
    url('',include(router.urls)),
]