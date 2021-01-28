from django.db import models


class Tag(models.Model):
    TAG_CHOICES = (
        ('Завтрак', 'Завтрак'),
        ('Обед', 'Обед'),
        ('Ужин', 'Ужин'),
    )
    title = models.CharField('Название', max_length=50, choices=TAG_CHOICES)
    # slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    # def __str__():
    #     return self.title
