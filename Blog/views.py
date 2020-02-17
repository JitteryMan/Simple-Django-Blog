from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Tag


def init_with_tag() -> dict:
    return {'tags': Tag.objects.order_by('tag_name')}


def index(request):
    list_ = init_with_tag()
    posts = Post.objects.order_by('-date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        post_page = paginator.page(1)
    except EmptyPage:
        post_page = paginator.page(paginator.num_pages)
    list_.update({'post_list': post_page})
    return render(request, 'Blog/page.html', list_)


def detail(request, post_uuid):
    try:
        list_ = init_with_tag()
        uuid = Post.objects.get(uuid=post_uuid)
        uuid.view += 1
        uuid.save()
        list_.update({'uuid': uuid})
        list_.update({'comments': uuid.comment_set.order_by('-id')})
    except Exception:
        raise Http404('Статья не найдена!')
    return render(request, 'Blog/page-detail.html', list_)


def leave_comment(request, post_uuid):
    try:
        uuid = Post.objects.get(uuid=post_uuid)
    except Exception:
        raise Http404('Статья не найдена!')
    uuid.comment_set.create(author=request.POST['aname'], body=request.POST['atext'])
    return HttpResponseRedirect(reverse('blog:detail', args=(uuid.uuid, )))


def search(request, label):
    try:
        list_ = init_with_tag()
        if request.GET.get('q', ''):
            label = request.GET.get('q', '')
            posts = Post.objects.filter(title__contains=label).order_by('-date')
            if not posts:
                list_.update({'search_list': Post.objects.filter(body__contains=label).order_by('-date'), 'label': label})
            else:
                list_.update({'search_list': posts, 'label': label})
        else:
            list_.update({'search_list': Post.objects.filter(tag__tag_name__contains=label).order_by('-date'),
                          'label': label})
    except Exception:
        raise Http404('Статьи не найдены!')
    return render(request, 'Blog/search-page.html', list_)

