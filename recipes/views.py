from django.http.response import Http404
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Recipe
from utils.pagination import make_pagination
import os
# HTTP Request
PER_PAGES = int(os.environ.get('PER_PAGE', 6))


class RecipeListViewBase(ListView):
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = None
    ordering = ['-id']
    template_name = 'recipes/pages/home.html'

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(
            is_published=True
        )

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        page_obj, pagination_range = make_pagination(
            self.request, context.get('recipes'), PER_PAGES)

        context.update({'recipes': page_obj, 'pagination_range': pagination_range})
        return context


class RecipeListViewHome(RecipeListViewBase):
    template_name = 'recipes/pages/home.html'


class RecipeListViewCategory(RecipeListViewBase):
    template_name = 'recipes/pages/category.html'

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(
            category__id=self.kwargs.get('category_id'), is_published=True
        )

        if not queryset:
            raise Http404()

        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': f'{context.get("recipes")[0].category.name} |'
        })

        return context


class RecipeListViewSearch(RecipeListViewBase):
    template_name = 'recipes/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('search', '')

        if not search_term:
            raise Http404()

        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(
            Q(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term),
            ), is_published=True
        )

        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('search', '')

        context.update({
            'page_title': f'Search for "{search_term}" |',
            'search_term': search_term,
            'additional_url_query': f'&search={search_term}'
        })

        return context


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/pages/recipe-view.html'

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(is_published=True)

        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context.update({
            'is_detail_page': True
        })

        return context
