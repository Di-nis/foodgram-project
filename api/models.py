from django.contrib.auth import get_user_model
from django.db import models

from recipes.models import Recipe

User = get_user_model()



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

    def __str__(self):
        return '{} - {}'.format(self.user, self.author)

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

    def __str__(self):
        return '{} - {}'.format(self.user, self.recipe)

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

    def __str__(self):
        return '{} - {}'.format(self.user, self.recipe)

    class Meta:
        unique_together = ['user', 'recipe']
        verbose_name = 'Рецепты (покупка)'
        verbose_name_plural = 'Рецепты (покупка)'
