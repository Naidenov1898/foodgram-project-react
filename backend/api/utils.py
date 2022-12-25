# from django.db.models import F, Sum
# from django.http.response import HttpResponse
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.status import HTTP_400_BAD_REQUEST

# from recipes.models import IngredientAmount


# @action(methods=('GET',), detail=False)
# def download_shopping_cart(self, request):
#     user = self.request.user
#     if not user.carts.exists():
#         return Response(status=HTTP_400_BAD_REQUEST)
#     ingredients = IngredientAmount.objects.filter(
#         recipe__in=(user.carts.values('id'))
#     ).values(
#         ingredient=F('ingredients__name'),
#         measure_unit=F('ingredients__measurement_unit')
#     ).annotate(amount_cart=Sum('amount'))
#     filename = f'{user.username}_shopping_list.txt'
#     shopping_list = 'Список покупок\n'

#     for ingr in ingredients:
#         shopping_list += (
#             f'{ingr["ingredient"]}: '
#             f'{ingr["amount_cart"]} '
#             f'{ingr["measure_unit"]}\n'
#         )
#     response = HttpResponse(
#         shopping_list, content_type='text.txt; charset=utf-8'
#     )
#     response['Content-Disposition'] = (
#         f'attachment; filename={filename}.txt'
#     )
#     return response
