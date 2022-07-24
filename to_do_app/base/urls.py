from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from to_do_app.base.views import home_page, dashboard_page

urlpatterns = [
    path('', home_page, name='home page'),
    path('dashboard/', dashboard_page, name='dashboard page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
