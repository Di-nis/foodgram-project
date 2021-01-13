from django.db import models
from users.models import User
from tags.models import Tag


class Ingredient(models.Model):
    '''Инградиенты'''
    name = models.CharField(max_length=200, verbose_name='Название')
    count = models.PositiveSmallIntegerField()
    # measure = model.ChoiceField()

    class Meta:
        verbose_name = 'Инградиент'
        verbose_name_plural = 'Инградиенты'

    def __str__(self):
        return '{}'.format(self.name)


class Recipe(models.Model):
    '''Рецепты'''
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание')
    ingredients = models.ManyToManyField(
        Ingredient,
        # through='',
        # through_fields=(),
        related_name='recipes',
        # verbose_name='Инградиент',
        # verbose_name_plural = 'Инградиенты'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipes')
    time = models.TimeField()
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return '{}'.format(self.name)
