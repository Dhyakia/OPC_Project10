from django.contrib import admin
from django.urls import path, include

from users.views import CreateUserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', CreateUserAPIView.as_view())

]
