"""quizApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from users import views as users_views
from materials import views as materials_views
from quizzes import views as quizzes_view


router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='user')
router.register(r'class', materials_views.ClassViewSet, basename='class')
router.register(r'subject', materials_views.SubjectViewSet, basename='subject')
router.register(r'study-material', materials_views.StudyMaterialViewSet, basename='studymaterial')
router.register(r'quiz', quizzes_view.QuizViewSet, basename='quizzes')
router.register(r'questions', quizzes_view.QuestionsViewSet, basename='questions')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', users_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/quiz-details/',quizzes_view.QuizDetailViewSet.as_view(),name='token_pair')
]
