from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article
# Create your views here.

# class base view
class BlogArticleCreateView(CreateView):
    # unique identifier
    template_name = "articles/blog_article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all() # blog/<modulename>_list.html
    # success_url = '/'

    def for_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class BlogArticleListView(ListView):
    # unique identifier
    model = Article
    template_name = "articles/blog_article_list.html"
    # define the object name
    context_object_name = 'object'
    queryset = Article.objects.all() # blog/<modulename>_list.html



class BlogArticleDetailView(DetailView):
    template_name = "articles/blog_article_detail.html"
    # queryset will become the object in your template
    queryset = Article.objects.all() # blog/<modulename>_detail.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Log out the current id
        print(f"id = ${kwargs.get('pk')}")
        context["object"] = get_object_or_404(Article.objects.filter(id=self.kwargs.get('pk')))

        return context

class BlogArticleUpdateView(UpdateView):
    # unique identifier
    template_name = "articles/blog_article_create.html"
    form_class = ArticleModelForm
    queryset: Article.objects.all()
    
    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=pk_)

    def for_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BlogArticleDeleteView(DeleteView):
    # unique identifier
    template_name = "articles/blog_article_delete.html"

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=pk_)
    
    def get_success_url(self):
        return reverse('blog:blog_article_list', kwargs={})
    
# function based view
def blog_main_view(request, *args, **kwargs):
    return HttpResponse("<h1>Blog Main</h1>")

def blog_article_view(request, *args, **kwargs):
    context = { }
    return render(request, 'articles/blog_article.html', context)

# convert to class base view
class BlogMainView(View):
    html_elements = "<h1>Blog Main</h1>"

    queryset = Article.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.html_elements)

    # def post(request, *args, **kwargs):
    #     return HttpResponse("<h1>Blog Main</h1>")
