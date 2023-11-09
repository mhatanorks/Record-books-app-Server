from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    # path("api/auth/", include("dj_rest_auth.urls")), # 追加
    path("api/social/login/", include("accounts.urls")), # 追加
    path("", include("app.urls")),
]
