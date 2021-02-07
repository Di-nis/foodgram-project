from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe, RecipeIngredient, Tag

User = get_user_model()


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


def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    recipes = user_profile.recipes.all()
    tag_list = Tag.objects.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/profile.html', {
        'page': page,
        'paginator': paginator,
        'user_profile': user_profile,
        'tag_list': tag_list
        }
    )


@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST,
                          files=request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('index')
        return render(
            request, 'recipes/new_recipe.html', {
                'form': form,
            }
        )
    form = RecipeForm()
    return render(request, 'recipes/new_recipe.html', {
        'form': form,
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
        form_edited = RecipeForm(request.POST or None,
                                 files=request.FILES or None,
                                 instance=recipe)
        if form_edited.is_valid():
            form_edited.save()
            return redirect('recipe',
                            recipe_id=recipe.id)
        return render(request, 'recipes/new_recipe.html', {
            'form': form_edited,
            'recipe': recipe,
            }
        )
    return redirect('index')


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author == request.user:
        Recipe.objects.get(id=recipe_id).delete()
        return redirect('index')


@login_required
def favorite_recipes(request):
    recipe_list = Recipe.objects.filter(
        favorite__user=request.user
    )
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


@login_required
def shop_list(request):
    recipe_list = Recipe.objects.filter(
        purchase__user=request.user
    )
    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/shop_list.html', {
        'page': page,
        'paginator': paginator
        }
    )


@login_required
def follow_index(request):
    user_list = User.objects.filter(
        following__user=request.user).order_by('id')
    paginator = Paginator(user_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/MyFollow.html', {
        'page': page,
        'paginator': paginator
        }
    )


def tag_filter(request, display_name):
    recipe_list = Recipe.objects.filter(
        tags__display_name=display_name)
    tag_list = Tag.objects.all()
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_filter.html', {
        'page': page,
        'paginator': paginator,
        'tag_list': tag_list,
        'display_name': display_name
        }
    )


@login_required
def download(request):
    ingredients = RecipeIngredient.objects.filter(
        recipe__in=Recipe.objects.filter(
            purchase__user=request.user
        )
    )
    shop_list = {}
    text_output = ''

    for res in ingredients:
        shop_list[res.ingredient.name] = [0, res.ingredient.dimension]

    for res in ingredients:
        try:
            shop_list[res.ingredient.name][0] += res.amount
        except TypeError:
            pass

    for res in shop_list:
        text_output += f'{res} - {shop_list[res][0]} {shop_list[res][1]}\n'
    response = HttpResponse(text_output, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="shop_list.txt"'
    return response


def page_not_found(request, exception):
    return render(request, "misc/404.html",
                  {"path": request.path},
                  status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)
