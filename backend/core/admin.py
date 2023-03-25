from django.contrib import admin

from .models import ImageAlbum


class ImageAlbumInline(admin.TabularInline):
    model = ImageAlbum
    extra = 3