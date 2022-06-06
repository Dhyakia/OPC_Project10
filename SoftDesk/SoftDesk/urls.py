from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views as userV
from projects import views as projectsV

# projects/
# projects/<pk>/
router = routers.SimpleRouter()
router.register(r'projects', projectsV.ProjectsViewset)

# projects/<projects_pk>/users/
# projects/<projects_pk>/users/<pk>/
projects_user_router = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
projects_user_router.register(r'users', projectsV.ContributorsViewset)

# projects/<projects_pk>/issues/
# projects/<projects_pk>/issues/<pk>/
projects_issue_router = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
projects_issue_router.register(r'issues', projectsV.IssuesViewset)

# projects/<projects_pk>/issues/<issues_pk>/comments/
# projects/<projects_pk>/issues/<issues_pk>/comments/<pk>/
projects_issue_comment_router = routers.NestedSimpleRouter(projects_issue_router, r'issues', lookup='issues')
projects_issue_comment_router.register(r'comments', projectsV.CommentsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', userV.CreateUserAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'', include(router.urls)),
    path(r'', include(projects_user_router.urls)),
    path(r'', include(projects_issue_router.urls)),
    path(r'', include(projects_issue_comment_router.urls))
    
]