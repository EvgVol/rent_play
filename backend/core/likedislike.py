from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from users.models import User


class LikeDislikeManager(models.Manager):
    """Менеджер по сбору лайков и дизлайков."""

    use_for_related_fields = True
 
    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)
 
    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)
 
    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(models.Sum('vote')).get('vote__sum') or 0
    
    def consoles(self):
        return self.get_queryset().filter(content_type__model='console').order_by('-consoles__pub_date')


class LikeDislike(models.Model):
    """Модель лайков."""

    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField('Голос', choices=VOTES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             verbose_name='Пользователь')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()
