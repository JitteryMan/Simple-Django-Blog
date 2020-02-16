from enum import auto

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils.translation import gettext as _
from .models import Post, Tag


def init_with_tag() -> dict:
    return {'tags': Tag.objects.order_by('tag_name')}


def index(request):
    print('index')
    list_ = init_with_tag()
    list_.update({'post_list': Post.objects.order_by('-date')})
    return render(request, 'Blog/page.html', list_)


def detail(request, post_uuid):
    try:
        print('detail')
        list_ = init_with_tag()
        uuid = Post.objects.get(uuid=post_uuid)
        uuid.view += 1
        uuid.save()
        print(uuid.view)
        list_.update({'uuid': uuid})
        list_.update({'comments': uuid.comment_set.order_by('-id')})
    except Exception:
        raise Http404('Статья не найдена!')
    return render(request, 'Blog/page-detail.html', list_)


def leave_comment(request, post_uuid):
    try:
        print('leave_comment')
        uuid = Post.objects.get(uuid=post_uuid)
        print(leave_comment)
    except Exception:
        raise Http404('Статья не найдена!')
    uuid.comment_set.create(author=request.POST['aname'], body=request.POST['atext'])
    return HttpResponseRedirect(reverse('blog:detail', args=(uuid.uuid, )))


def search(request, label):
    try:
        print('search')
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

