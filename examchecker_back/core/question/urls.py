from rest_framework.routers import DefaultRouter
from examchecker_back.core.question import views

router = DefaultRouter()

router.register(r'question', views.QuestionViewSet, basename='question')
router.register(r'answer', views.ChoiceViewSet, base_name='answer')
urlpatterns = router.urls