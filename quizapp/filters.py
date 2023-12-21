from django_filters import FilterSet, CharFilter, NumberFilter, NumericRangeFilter
from .models import Result
from django import forms


class ResultFilter(FilterSet):
    total_ball = NumberFilter(lookup_expr='icontains', label='Title',
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    first_name = CharFilter(lookup_expr='icontains', label='first_name',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = CharFilter(lookup_expr='icontains', label='last_name',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    balls = NumericRangeFilter(lookup_expr='icontains', label='range',
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Result
        fields = ['total_ball', 'first_name', 'last_name', 'balls']
