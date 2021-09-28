import django_filters
from .models import Post

# original
class PostFilter(django_filters.FilterSet):


    class Meta:
        model = Post
        fields = {
                   'title': ['icontains'],
                   'body': ['icontains'],
        }

# class PostFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     body = django_filters.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = Post
#         fields = [
#                    'title',
#                     'body'
#         ]


