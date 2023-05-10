from django import forms

from .models import Post, Comment, Review


class PostForm(forms.ModelForm):
    """Форма создание поста."""

    class Meta:
        model = Post
        fields = ('name','description', 'game', 'image',)
        labels = {'name': 'Заголовок',
                  'description': 'Текст',
                  'game': 'Игра',
                  'image': 'Изображение'
        }
        help_texts = {
            'name': 'Введите заголовок',
            'description': 'Введите текст сообщения',
            'game': 'Выберите игру, к которой принадлежит это сообщение',
            'image': 'Выберите своё изображение которым хотите поделиться'
        }


class ReviewForm(forms.ModelForm):
    """Форма создание отзыва."""

    class Meta:
        model = Review
        labels = {"text": "Текст"}
        fields = ('text',)
        help_texts = {
            'text': 'Текст отзыва к посту'
        }


class CommentForm(forms.ModelForm):
    """Форма создание комментария."""

    class Meta:
        model = Comment
        labels = {"text": "Текст"}
        fields = ('text',)
        help_texts = {
            'text': 'Текст нового комментария'
        }
