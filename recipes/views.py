from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Recipe, User, Ingredient, Follow, Favorite
from tags.models import Tag
from .forms import RecipeForm, IngredientForm
import pandas as pd
from rest_framework import filters, permissions, viewsets
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from .serializers import FollowSerializer
from .permissions import IsStaffOrOwner
from excel_response import ExcelResponse


class BaseCreateDestroyViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


def index(request):
    recipe_list = Recipe.objects.all()
    tag_list = Tag.objects.all()
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/index.html', {
        'page': page,
        'paginator': paginator,
        'tag_list': tag_list
        }
    )

# def profile(request, username):
def profile(request, id):
    # user_profile = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(User, id=id)
    recipes = user_profile.recipes.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/profile.html', {
        'page': page,
        'paginator': paginator,
        'user_profile': user_profile,
        }
    )

@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('index')
        return render(
            request, 'recipes/new_recipe.html', {
                'form': form,
                'is_created': True,
            }
        )
    form = RecipeForm()
    return render(request, 'recipes/new_recipe.html', {
        'form': form,
        'is_created': True,
        }
    )


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe.html', {
        'recipe': recipe,
        # 'user_profile': post_profile.author,
        }
    )


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    form = RecipeForm(instance=recipe)
    if recipe.author == request.user:
        form_edited = RecipeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=recipe
        )
        if form_edited.is_valid():
            form_edited.save()
            return redirect('recipe',
                            recipe_id=recipe.id)
        return render(request, 'recipes/new_recipe.html', {
            'form': form,
            'recipe': recipe,
            }
        )
    return redirect('index')


@login_required
def favorite_recipes(request):
    recipe_list = Recipe.objects.filter(favorite__user=request.user)
    tag_list = Tag.objects.all()
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/favorite.html', {
        'page': page,
        'paginator': paginator,
        'tag_list': tag_list
        }
    )

def recipes_filter(request, tag_id):
    recipe_list = Recipe.objects.filter(tags__id=tag_id)
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_filter.html', {
        'page': page,
        'paginator': paginator
        }
    )


# @login_required
# def add_recipe_favorite(request, recipe_id):
#     recipe = get_object_or_404(Recipe, id=recipe_id)
#     Favorite.objects.get_or_create(user=request.user, recipe=recipe)
#     return redirect('shop_list')


# @login_required
# def delete_recipe_favorite(request, recipe_id):
#     recipe = get_object_or_404(Recipe, id=recipe_id)
#     Favorite.objects.get_or_create(user=request.user, recipe=recipe).delete()
#     return redirect('shop_list')


@login_required
def shop_list(request):
    recipe_list = Recipe.objects.filter(purchase__user=request.user)
    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/shop_list.html', {
        'page': page,
        'paginator': paginator
        }
    )

@login_required
def new_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            # recipe.author = request.user
            recipe.save()
            return redirect('index')
        return render(
            request, 'recipes/new_recipe.html', {
                'form_ingredient': form,
                # 'is_created': True,
            }
        )
    form = RecipeForm()
    return render(request, 'recipes/new_recipe.html', {
        'form_ingredient': form,
        # 'is_created': True,
        }
    )


@login_required
def follow_index(request):
    recipe_list = Recipe.objects.filter(
        author__following__in=Follow.objects.filter(user=request.user))
    paginator = Paginator(recipe_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/follow.html', {
        'page': page,
        'paginator': paginator
        }
    )

class FollowsViewSet(BaseCreateDestroyViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # filter_backends = [filters.SearchFilter]
    permission_classes = [IsStaffOrOwner, ]
    # search_fields = ['=name', ]
    # lookup_field = 'slug'


# @login_required
# def profile_follow(request, username):
#     pass
    # user = get_object_or_404(User, username=username)
    # if request.user != user and Follow.objects.filter(
    #         user=User.objects.get(username=request.user.username),
    #         author=User.objects.get(username=user.username)).count() == 0:
    #     Follow.objects.get_or_create(user=request.user, author=user)
    #     return redirect('profile', username=user.username)
    # return redirect('profile', username=user.username)


# @login_required
# def profile_unfollow(request, username):
#     pass
    # user = get_object_or_404(User, username=username)
    # if Follow.objects.filter(
    #         user=User.objects.get(username=request.user.username),
    #         author=User.objects.get(username=user.username)).count() != 0:
    #     Follow.objects.get(user=request.user, author=user).delete()
    #     return redirect('profile', username=user.username)
    # return redirect('profile', username=user.username)


def download(request):
    list = [[], []]
    recipe_list = Recipe.objects.filter(purchase__user=request.user)
    for recipe in recipe_list:
        list[0]+=[recipe.name]
        list[1]+=[recipe.description]
    shop_list = [['Column 1', 'Column 1'], 
                 list[0],
                 list[1]
                ]
    return ExcelResponse(shop_list, 'shop_list')


def page_not_found(request, exception):
    return render(
        request, 
        "misc/404.html", 
        {"path": request.path}, 
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500) 
