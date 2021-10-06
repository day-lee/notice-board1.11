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
    template_name = 'board/post_list.html'
    ordering = ['-post_created']
    paginate_by = 5

    # def get_queryset(self):
    #     queryset = super(PostListView, self).get_queryset()
    #     filter = PostFilter(self.request.GET, queryset)
    #     return filter.qs


# title 과 body 를 같이 검색하려면 get_queryset, get_context_data, Q를 이용해야함
#     def get_queryset(self):
#         search_keyword = self.request.GET.get('q', '')
#         search_type = self.request.GET.get('type', '')
#         notice_list = Post.objects.order_by('-id')
#
#         if search_keyword:
#             if len(search_keyword) > 1:
#                 if search_type == 'all':
#                     search_notice_list = notice_list.filter(
#                         Q(title__icontains=search_keyword) | Q(body__icontains=search_keyword) | Q(
#                             author__user_id__icontains=search_keyword))
#                 elif search_type == 'title_content':
#                     search_notice_list = notice_list.filter(
#                         Q(title__icontains=search_keyword) | Q(body__icontains=search_keyword))
#                 elif search_type == 'title':
#                     search_notice_list = notice_list.filter(title__icontains=search_keyword)
#                 elif search_type == 'body':
#                     search_notice_list = notice_list.filter(body__icontains=search_keyword)
#                 elif search_type == 'author':
#                     search_notice_list = notice_list.filter(author__user_id__icontains=search_keyword)
#
#                 return search_notice_list
#             else:
#                 messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
#         return notice_list
#
#     def get_context_data(self, **kwargs):
#         search_keyword = self.request.GET.get('q', '')
#         search_type = self.request.GET.get('type', '')
#
#         if len(search_keyword) > 1:
#             context['q'] = search_keyword
#         context['type'] = search_type
#
#         return context

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
