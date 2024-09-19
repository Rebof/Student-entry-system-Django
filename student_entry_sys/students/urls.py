from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, student_create, student_list, student_update, student_delete

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API URLs
    path('', student_list, name='student_list'),  # Root URL maps to student_list
    path('create/', student_create, name='student_create'),
    path('<int:pk>/edit/', student_update, name='student_update'),
    path('<int:pk>/delete/', student_delete, name='student_delete'),
]