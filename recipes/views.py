import pandas as pd
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from excel_response import ExcelResponse

from .forms import IngredientForm, RecipeForm
from .models import Recipe, Tag
from .utils import make_doc
from django.http import FileResponse

User = get_user_model()
TAGS = ['breakfast', 'lunch', 'dinner']

def index(request):
    recipe_list = Recipe.objects.all()
    tags = request.GET.getlist('tag', TAGS)
    print('Тест', request.GET.getlist)
    print(tags)
    # tag_list=Tag.objects.prefetch_related('recipes')
    tag_list=Tag.objects.all()
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
    recipe_list = Recipe.objects.filter(
        favorite__user=request.user)
    tag_list = Tag.objects.filter(
        recipes__in=Recipe.objects.filter(
            favorite__user=request.user))
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/favorite.html', {
        'page': page,
        'paginator': paginator,
        'tag_list': tag_list
        }
    )


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
    user_list = User.objects.filter(following__user=request.user)
    paginator = Paginator(user_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/MyFollow.html', {
        'page': page,
        'paginator': paginator
        }
    )


def download(make_doc):
    return FileResponse(make_doc, as_attachment=True, filename='Shop_list.pdf')


def page_not_found(request, exception):
    return render(
        request, 
        "misc/404.html", 
        {"path": request.path}, 
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500) 
