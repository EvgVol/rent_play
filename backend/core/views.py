from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage

from .forms import FeedbackCreateForm
from .models import Feedback

class HomeView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class ServiceView(TemplateView):
    template_name = "core/services.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = 'Ваше письмо успешно отправлено!'
    template_name = 'core/feedback.html'
    success_url = reverse_lazy('core:feedback_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.send_notification_email()
        return response

class FeedbackSuccessView(TemplateView):
    template_name = 'core/feedback_success.html'