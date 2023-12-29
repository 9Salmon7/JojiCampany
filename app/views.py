from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class MainView(TemplateView):
	template_name = "index.html"

class BusinessView(TemplateView):
	template_name = "Business.html"

class NewsView(TemplateView):
	template_name = "News.html"

class SustainabilityView(TemplateView):
	template_name = "Sustainability.html"

class RecruitmentView(TemplateView):
	template_name = "Recruitment.html"

class ContactView(TemplateView):
	template_name = "Contact.html"


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")
