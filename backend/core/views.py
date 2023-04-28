from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class ServiceView(TemplateView):
    template_name = "core/services.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


