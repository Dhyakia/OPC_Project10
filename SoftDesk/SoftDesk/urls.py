from django.contrib import admin
from django.urls import path, include

from users import views as userV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', userV.CreateUserAPIView.as_view()),
    path('login/', userV.authenticate_user, name='obtain-token')

]
