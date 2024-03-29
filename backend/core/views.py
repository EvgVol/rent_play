from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import FeedbackCreateForm
from .models import Feedback
from .utils import get_client_ip
from .email import send_contact_email_message


class HomeView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class ServiceView(TemplateView):
    template_name = "core/services.html"


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            if self.request.user.is_authenticated:
                feedback.user = self.request.user
            send_contact_email_message(feedback.name, feedback.subject,
                                       feedback.email, feedback.content,
                                       feedback.ip_address, feedback.user_id)
        return super().form_valid(form)

