from django.urls import path
from rest_framework import routers

from api1.views import ServicesAPiView, get_set_service, get_person, get_house, get_city

# from api1.views import SalonView, ServiceView, CategoryView, get_categoryes, get_service, get_service_for_title

# router = routers.SimpleRouter()
# router.register(r'view-salon', SalonView)
# router.register(r'serviceView', ServiceView)
# router.register(r'categoryView', CategoryView)
# urlpatterns = router.urls


app_name = "api1"
urlpatterns = [
    # path('categoryes/', get_categoryes),
    # path('service/', get_service),
    # path('salones/', SalonView.as_view()),
    # path('serviсes/<str:text>', get_service_for_title),
    # APIView урлы для апивью
    path('servicesApiView/', ServicesAPiView.as_view()),
    path('get_post_services/', get_set_service),
    path('house/', get_house),
    path('house/<int:pk>', get_house),
    path('person/', get_person),
    path('person/<int:pk>/', get_person),
    path('city/', get_city),
    path('city/<int:pk>/', get_city),
    ]
