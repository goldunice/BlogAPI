from django.contrib import admin
from django.urls import path, include
from blogApp.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("maqolalar", MaqolalarModleViewSet)

urlpatterns = [
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Maqolalar/', MaqolalarAPI.as_view()),
    path('Maqolalar/<int:pk>/', MaqolaAPIView.as_view())
]
