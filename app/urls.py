from django.urls import path
from app import views
from .views import MainView, BusinessView, NewsView, SustainabilityView, RecruitmentView, ContactView

urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path('business/', BusinessView.as_view()),
    	path('news/', NewsView.as_view()),
    	path('Sustainability/', SustainabilityView.as_view()),
    	path('Recruitment/', RecruitmentView.as_view()),
    	path('Contact/', ContactView.as_view()),
]
