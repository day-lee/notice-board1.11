# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import PostFilter
#from .forms import PostForm, EditForm

from django.contrib import messages
from django.db.models import Q

class PostListView(ListView):
    model = Post
    #template_name = 'board/post_list.html'
    template_name = 'board/post_list_filter.html'
    ordering = ['-post_created']
    paginate_by = 5
    context_object_name = 'object_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        object_list = Post.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_object_list = object_list.filter(
                        Q(title__icontains=search_keyword) | Q(body__icontains=search_keyword)
                        | Q(author__username__icontains=search_keyword))
                elif search_type == 'title_body':
                    search_object_list = object_list.filter(
                        Q(title__icontains=search_keyword) | Q(body__icontains=search_keyword))
                elif search_type == 'title':
                    search_object_list = object_list.filter(title__icontains=search_keyword)
                elif search_type == 'body':
                    search_object_list = object_list.filter(body__icontains=search_keyword)
                elif search_type == 'author__username':
                    search_object_list = object_list.filter(author__username__icontains=search_keyword)
                return search_object_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return object_list

    def get_context_data(self, **kwargs):
        #pagination
        context = super(PostListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index
        page_range = paginator.page_range #[start_index:end_index]
        context['page_range'] = page_range

        #filter
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        notice_fixed = Post.objects.all().order_by('-id')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type
        context['notice_fixed'] = notice_fixed

        return context

# title, body 각각 검색
    # def get_queryset(self):
    #     queryset = super(PostListView, self).get_queryset()
    #     filter = PostFilter(self.request.GET, queryset)
    #     return filter.qs


class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'board/post_form.html'

    #template_name = 'board/post_form_feedback.html'
    #templatfor updated JS: currently not working

    fields = '__all__'
    #form_class = PostForm #returns 'FileField' object has no attribute 'use_required_attribute' error


class PostTestView(CreateView):
    model = Post
    template_name = 'board/form_js_test.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'board/post_form_django.html'

    #template_name = 'board/post_form.html'
    # 'post_form' returns nothing.
    # The reason why 'form.html' in 'post_form_django.html' works is because 'html element in 'post_form' is copied from developers tool


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'board/post_confirm_delete.html'
    success_url = reverse_lazy('board:notice-board')
