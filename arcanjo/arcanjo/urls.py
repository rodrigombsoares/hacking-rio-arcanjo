from django.urls import include, path
from rest_framework import routers
from api import views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('message', views.MessageViewset.as_view(), name='message'),
    path('consult/<int:session_id>/<int:start>/', views.ConsultationView.as_view(), name='consult'),
    path('info/<int:session_id>/', views.InfoView.as_view(), name='info'),
    path('sort/<int:session_id>/', views.SortingView.as_view(), name='sort'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)