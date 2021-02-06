from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    TAG_CHOICES = (
        ('Завтрак', 'Завтрак'),
        ('Обед', 'Обед'),
        ('Ужин', 'Ужин'),
    )
    title = models.CharField(
        'Название',
        max_length=50,
        choices=TAG_CHOICES,
        unique=True
    )
    display_name = models.CharField(
        'Имя тега в шаблоне',
        max_length=20,
    )
    color = models.CharField(
        'Цвет тега',
        max_length=20,
    )

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        unique=True
    )
    dimension = models.CharField(
        'Единица измерения',
        max_length=10,
    )

    def __str__(self):
        return '{} {}'.format(self.name, self.dimension)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    title = models.CharField(
        'Название рецепта',
        max_length=200
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name = 'Теги',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name = 'Инградиент'
    )
    prep_time = models.PositiveSmallIntegerField(
        'Время приготовления (в минутах)',
    )
    description = models.TextField(
        'Инструкция по приготовлению',
        max_length=1000,
    )
    image = models.ImageField(
        "Изображение",
        upload_to='recipes/',
    )
    pub_date = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True
    )
    slug = AutoSlugField(
        populate_from='title',
        allow_unicode=True
    )

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='numbers',
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amounts',
        verbose_name='Рецепт'
    )
    amount = models.FloatField(
        "Количество",
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{} {}'.format(
            self.ingredient, self.amount)

    class Meta:
        verbose_name = 'Ингредиент (рецепт)'
        verbose_name_plural = 'Ингредиенты (рецепт)'
