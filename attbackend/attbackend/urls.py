from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from attapi import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/v1/users', views.UserViewSet)
router.register(r'api/v1/userinfos', views.UserInfoViewSet)
router.register(r'api/v1/subjects', views.SubjectViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'attbackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
