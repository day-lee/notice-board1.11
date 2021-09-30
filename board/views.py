# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import PostFilter
#from .forms import PostForm, EditForm

class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    ordering = ['-post_created']
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        filter = PostFilter(self.request.GET, queryset)
        return filter.qs


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
