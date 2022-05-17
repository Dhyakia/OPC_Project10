from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views as userV
from projects import views as projectsV


router = routers.SimpleRouter()
router.register('projects', projectsV.ProjectsViewset, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', userV.CreateUserAPIView.as_view(), name='signup'),
    path('api/', include(router.urls)),
    
]
