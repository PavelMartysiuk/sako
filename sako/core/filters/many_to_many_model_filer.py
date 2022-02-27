from django_filters import rest_framework as filters


class CharFilerInFilter(filters.BaseInFilter, filters.CharFilter):
    pass
