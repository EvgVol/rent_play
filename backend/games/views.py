from django.views.generic import TemplateView


class GamesView(TemplateView):
    template_name = "games/games.html"


class GameDetailView(TemplateView):
    template_name = "games/game-detail.html"
