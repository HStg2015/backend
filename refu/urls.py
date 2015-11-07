from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'refugee_camp', views.RefugeeCampViewSet)
router.register(r'object_category', views.ObjectCategoryViewSet)
router.register(r'object_sub_category', views.ObjectSubCategoryViewSet)
router.register(r'simple_offer', views.SimpleOfferViewSet)
router.register(r'help_time_search', views.HelpTimeSearchViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^files/', include('db_file_storage.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
