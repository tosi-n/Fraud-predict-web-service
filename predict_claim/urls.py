from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('predict_claim', views.User_InputView),
urlpatterns = [
    path('api/', include(router.urls)),
    path('fraud_claim/', views.predict),
]