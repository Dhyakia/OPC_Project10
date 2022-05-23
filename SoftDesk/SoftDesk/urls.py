from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views as userV
from projects import views as projectsV


router = routers.SimpleRouter()
router.register(r'projects', projectsV.ProjectsViewset)

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
projects_router.register(r'users', projectsV.ContributorsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', userV.CreateUserAPIView.as_view(), name='signup'),
    path(r'', include(router.urls)),
    path(r'', include(projects_router.urls))
    
]