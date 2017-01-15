from django.conf.urls import url, include
from contacts.views import ContactViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('contacts', ContactViewset)


urlpatterns = [
    url(r'^', include(router.urls))
]