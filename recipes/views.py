from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe, RecipeIngredient
from .utils import edit_recipe, save_recipe


User = get_user_model()
TAGS = ["breakfast", "lunch", "dinner"]


def index(request):
    search_query = request.GET.getlist("tag", TAGS)
    recipe_list = Recipe.objects.filter(
        tags__display_name__in=search_query).distinct()
    paginator = Paginator(recipe_list, settings.PAGINATION_PAGE_SIZE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "recipes/index.html", {
        "page": page,
        "paginator": paginator,
        }
    )


def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    search_query = request.GET.getlist("tag", TAGS)
    recipes = user_profile.recipes.filter(
        tags__display_name__in=search_query).distinct()
    paginator = Paginator(recipes, settings.PAGINATION_PAGE_SIZE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "recipes/profile.html", {
        "page": page,
        "paginator": paginator,
        "user_profile": user_profile,
        }
    )


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        save_recipe(request, form)
        return redirect("index")
    return render(request,
                  "recipes/new_recipe.html",
                  {"form": form}
                  )


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipes/recipe.html", {
        "recipe": recipe,
        }
    )


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        return redirect("index")
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None,
                      instance=recipe)
    if form.is_valid():
        edit_recipe(request, form, instance=recipe)
        return redirect("recipe", recipe_id=recipe.id)
    return render(request, "recipes/new_recipe.html", {
        "form": form,
        "recipe": recipe,
        }
    )


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
        return redirect("index")
    return redirect("recipe", recipe_id=recipe.id)


@login_required
def favorite_recipes(request):
    search_query = request.GET.getlist("tag", TAGS)
    recipe_list = Recipe.objects.filter(
        favorite__user=request.user,
        tags__display_name__in=search_query).distinct()
    paginator = Paginator(recipe_list, settings.PAGINATION_PAGE_SIZE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "recipes/favorite.html", {
        "page": page,
        "paginator": paginator,
        }
    )


@login_required
def shop_list(request):
    recipe_list = Recipe.objects.filter(
        purchase__user=request.user
    )
    return render(request, "recipes/shop_list.html", {
        "recipe_list": recipe_list
        }
    )


@login_required
def follow_index(request):
    user_list = User.objects.filter(
        following__user=request.user).order_by("-id")
    paginator = Paginator(user_list, settings.PAGINATION_PAGE_SIZE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "recipes/MyFollow.html", {
        "page": page,
        "paginator": paginator
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
    text_output = ""

    for res in ingredients:
        shop_list[res.ingredient.name] = [0, res.ingredient.dimension]

    for res in ingredients:
        try:
            shop_list[res.ingredient.name][0] += res.amount
        except TypeError:
            pass

    for res in shop_list:
        text_output += f"{res} - {shop_list[res][0]} {shop_list[res][1]}\n"
    response = HttpResponse(text_output, content_type="text/plain")
    response["Content-Disposition"] = 'attachment; filename="shop_list.txt"'
    return response
