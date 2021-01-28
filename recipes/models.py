from django.db import models
# from users.models import User
from tags.models import Tag
from django.contrib.auth import get_user_model


User = get_user_model()


class Ingredient(models.Model):
    '''Инградиенты'''
    name = models.CharField(max_length=200, verbose_name='Название')


    class Meta:
        verbose_name = 'Инградиент'
        verbose_name_plural = 'Инградиенты'

    def __str__(self):
        return '{}'.format(self.name)


class RecipeIngredient(models.Model):
    MEASURE_CHOICES = (
        ('г.', 'г.'),
        ('стакан', 'стакан'),
        ('кусок', 'кусок'),
        ('шт.', 'шт.'),
        ('по вкусу', 'по вкусу'), 
        ('ст.л.', 'ст.л.'),
        ('ч.л.', 'ч.л.'),
        ('мл.', 'мл.'),
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='numbers',
        verbose_name='Инградиент'
    )
    amount = models.IntegerField("Количество")
    measure = models.CharField(
        max_length=20,
        choices=MEASURE_CHOICES,
        default=None,
        verbose_name = 'Единица измерения'
    )

    class Meta:
        verbose_name = 'Инградиент (рецепт)'
        verbose_name_plural = 'Инградиенты (рецепт)'


class Recipe(models.Model):
    '''Рецепты'''
    TAG_CHOICES = (
        ('Завтрак', 'Завтрак'),
        ('Обед', 'Обед'),
        ('Ужин', 'Ужин'),
    )
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
    # tags = models.CharField(
    #     max_length=20,
    #     choices=TAG_CHOICES,
    #     default=None
    # )
    ingredients = models.ManyToManyField(
        RecipeIngredient,
        related_name='recipes',
        verbose_name = 'Инградиенты'
    )
    prep_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        # 'минут'
    )
    description = models.TextField(
        'Описание',
        max_length=500,
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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name='Подписка',
    )

    class Meta:
        unique_together = ['user', 'author']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite",
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorite",
        verbose_name='Рецепт'
    )

    class Meta:
        unique_together = ['user', 'recipe']
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="purchaser",
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="purchase",
        verbose_name='Рецепт'
    )

    class Meta:
        unique_together = ['user', 'recipe']
        verbose_name = 'Рецепты (покупка)'
        verbose_name_plural = 'Рецепты (покупка)'
