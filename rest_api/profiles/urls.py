from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, CreateProfileView, EditProfileView

router = DefaultRouter()
router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('profiles/create/', CreateProfileView.as_view()),
    path('profiles/update/', EditProfileView.as_view()),
    re_path('^', include(router.urls)),
]
