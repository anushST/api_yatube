from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .constants import API_VERSION
from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')

urlpatterns = [
    path(f'{API_VERSION}/', include(router_v1.urls)),
    path(f'{API_VERSION}/api-token-auth/', views.obtain_auth_token),
]
