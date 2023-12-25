from django.contrib import admin
from django.urls import path, include
from blogApp.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("maqolalar", MaqolalarModleViewSet)


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Blog_API loyihasi uchun Doc file',
        default_version='v1',
        description='Front-end, Android, Desktop dasturchilar uchun Blog-API DOCS',
        contact=openapi.Contact(email='AkmaljonGold@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)


urlpatterns = [
    path('swagger_doc_of_blog/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Maqolalar/', MaqolalarAPI.as_view()),
    path('Maqolalar/<int:pk>/', MaqolaAPIView.as_view())
]
