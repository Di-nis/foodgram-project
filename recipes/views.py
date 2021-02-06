from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe, RecipeIngredient, Tag

User = get_user_model()
TAGS = ['breakfast', 'lunch', 'dinner']

def index(request):
    recipe_list = Recipe.objects.all()
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

def profile(request, id):
    user_profile = get_object_or_404(User, id=id)
    recipes = user_profile.recipes.all()
    tag_list=Tag.objects.all()
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
        form = RecipeForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('index')
        return render(
            request, 'recipes/new_recipe.html', {
                'form': form,
                # 'is_created': True,
            }
        )
    form = RecipeForm()
    return render(request, 'recipes/new_recipe.html', {
        'form': form,
        # 'is_created': True,
        }
    )


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe.html', {
        'recipe': recipe,
        }
    )


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author == request.user:
        Recipe.objects.get(id=recipe_id).delete()
        return redirect('index')


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
            'is_created': True,
            }
        )
    # return redirect('index')


@login_required
def favorite_recipes(request):
    recipe_list = Recipe.objects.filter(
        favorite__user=request.user)
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

def download(request):
    ingredients = RecipeIngredient.objects.filter(
        recipe__in=Recipe.objects.filter(
            purchase__user=request.user
        )
    )
    purchases_list = {}

    for res in result:
        purchases[res.ingredient.name] = [0, res.ingredient.dimension]

    for res in ingredients:
        purchases[res.ingredient.name][0] += res.amount

    pass

    # return FileResponse(buffer, as_attachment=True, filename='Shop_list.pdf')


def page_not_found(request, exception):
    return render(
        request, 
        "misc/404.html", 
        {"path": request.path}, 
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500) 
