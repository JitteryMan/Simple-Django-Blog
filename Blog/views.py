from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.translation import gettext as _
from .models import Post, Tag


def init_with_tag() -> dict:
    return {'tags': Tag.objects.order_by('tag_name')}


def index(request):
    list_ = init_with_tag()
    list_.update({'post_list': Post.objects.order_by('-title')})
    return render(request, 'Blog/page.html', list_)


def detail(request, post_uuid):
    try:
        list_ = init_with_tag()
        list_.update({'uuid': Post.objects.get(uuid=post_uuid)})
    except Exception:
        raise Http404('Статья не найдена!')
    return render(request, 'Blog/page-detail.html', list_)


def django(request):
    # Translators: This message appears on the django page only
    a = _('Django is perfect')
    return HttpResponse(a)
