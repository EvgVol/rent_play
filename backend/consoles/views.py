from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import ConsoleForm


class ConsoleView(TemplateView):
    template_name = "consoles/consoles.html"


class ConsoleListView(TemplateView):
    template_name = "consoles/product-list.html"


class ConsoleDetailView(TemplateView):
    template_name = "consoles/product-detail.html"


class ConsoleCartView(TemplateView):
    template_name = "consoles/single-console.html"


class CheckoutView(TemplateView):
    template_name = "consoles/checkout.html"


class NewConsoleView(CreateView):
    """Вывод формы добавления консоли."""

    form_class = ConsoleForm
    template_name = 'consoles/new_console.html'
    success_url = '/thankyou/'
