from django.db import models


def get_upload_path(instance, filename):
    model = instance._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'

class Image(models.Model):
    """Абстрактная модель изображений."""

    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField('Изображение', upload_to=get_upload_path, blank=False)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'image'],
                name='unique_name_image',
            )
        ]
