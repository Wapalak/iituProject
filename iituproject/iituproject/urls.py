from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для панели администратора
    path('', include('main.urls')),  # Подключение URL-маршрутов из приложения main
    path('news/', include('news.urls'))  # Подключение URL-маршрутов из приложения news
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
