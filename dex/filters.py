import django_filters
from .models import Contact
from django_filters import CharFilter
from django.db.models import Q

class ContactFilter(django_filters.FilterSet):
    search = CharFilter(label='', method='my_lookup_method')

    def my_lookup_method(self, queryset, name, value):
            return queryset.filter(Q(contact_name__icontains=value)|Q(email__icontains=value)|Q(contact__icontains=value))


    