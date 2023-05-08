
from django.contrib import admin
from django.urls import path, include
from authentication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include("django.contrib.auth.urls")),
    path('authentication/', include("authentication.urls")),
    path('base/', include('base.urls')),
    path('register', views.register, name="register"),
    path('inventory/', include('inventory.urls'))
]
