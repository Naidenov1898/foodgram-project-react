from django_filters import rest_framework as filters
from recipes.models import Recipe
from rest_framework.filters import SearchFilter


class IngredientSearchFilter(SearchFilter):
    """
    Добавляет возможность поиска ингредиента
    по названию, при создании рецепта.
    """
    search_param = 'name'


class RecipeFilter(filters.FilterSet):
    """Кастомный фильтр для рецептов."""
    author = filters.CharFilter(
        field_name='author',
        method='filter_is_author'
    )
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = filters.BooleanFilter(
        field_name='is_favorited',
        method='filter_is_favorited'
    )
    is_in_shopping_cart = filters.BooleanFilter(
        field_name='is_in_shopping_cart',
        method='filter_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = (
            'author',
            'tags',
            'is_favorited',
            'is_in_shopping_cart'
        )

    def filter_is_favorited(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(favorite__user=self.request.user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(shopping_cart__user=self.request.user)
        return queryset

    def filter_is_author(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(aythor=self.request.user)
        else:
            return queryset.filter(author_id=value)
