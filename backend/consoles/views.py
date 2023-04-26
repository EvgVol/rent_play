from django.views.generic.edit import CreateView

from .forms import ConsoleForm


class ConsoleView(CreateView):
    """Вывод формы добавления консоли."""

    form_class = ConsoleForm
    template_name = 'consoles/new_console.html'
    success_url = '/thankyou/'
