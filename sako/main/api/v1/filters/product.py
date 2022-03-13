from django_filters import rest_framework as filters

from core.filters.many_to_many_model_filer import CharFilerInFilter

from main.models import Product


class ProductFilter(filters.FilterSet):
    category_ids = CharFilerInFilter(field_name='category')
    new = filters.BooleanFilter(field_name='new')
    manufactor = filters.NumberFilter(field_name='manufactor')
    availability = filters.BooleanFilter(field_name='availability')
    bestseller = filters.BooleanFilter(field_name='bestseller')

    class Meta:
        model = Product
        fields = (
            'category_ids',
            'manufactor',
            'availability',
            'bestseller'
        )
