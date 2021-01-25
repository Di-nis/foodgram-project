from django.db import models
# from users.models import User
from tags.models import Tag
from django.contrib.auth import get_user_model

User = get_user_model()

class Ingredient(models.Model):
    '''Инградиенты'''
    MEASURE_CHOICES = (
        ('грамм', 'г.'),
        ('стакан', 'стакан'),
        ('кусок', 'кусок'),
        ('штук', 'шт.'),
        ('по вкусу', 'по вкусу'), 
        ('столовые ложки', 'ст.л.'),
        ('чайные ложки', 'ч.л.'),
        ('миллилитр', 'мл.'),
    )
        
    name = models.CharField(max_length=200, verbose_name='Название')
    # count = models.PositiveSmallIntegerField()
    measure = models.CharField(
        max_length=20,
        choices=MEASURE_CHOICES,
        default=None
    )

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
    name = models.CharField(
        'Название рецепта',
        max_length=200
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name = 'Теги'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        verbose_name = 'Инградиенты'
    )
    ingredients_amount = models.PositiveSmallIntegerField(
        'Количество (объём)',
    )
    prep_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        # 'минут'
    )
    description = models.TextField(
        'Описание',
        # max_length=500,
        )
    image = models.ImageField(
        "Загрузить фото",
        upload_to='recipes/',
    )
    pub_date = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True
    )
    slug = models.SlugField(
        'Уникальный URL',
        unique=True,
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return '{}'.format(self.name)


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="follower"
    )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="following"
    )

    class Meta:
        unique_together = ['user', 'author']


class Favorite(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="purchaser"
    )
    recipe = models.ForeignKey(Recipe,
                             on_delete=models.CASCADE,
                             related_name="purchase"
    )

    class Meta:
        unique_together = ['user', 'recipe']
