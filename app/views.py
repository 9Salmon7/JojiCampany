from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class MainView(TemplateView):
	template_name = "app/index.html"

class BusinessView(TemplateView):
	template_name = "app/Business.html"

class NewsView(TemplateView):
	template_name = "app/News.html"

class SustainabilityView(TemplateView):
	template_name = "app/Sustainability.html"

class RecruitmentView(TemplateView):
	template_name = "app/Recruitment.html"

class ContactView(TemplateView):
	template_name = "app/Contact.html"
