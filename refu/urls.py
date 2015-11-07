from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'refugee_camp', views.RefugeeCampViewSet)
router.register(r'simple_offer', views.SimpleOfferViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^files/', include('db_file_storage.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
