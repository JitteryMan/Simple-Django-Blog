from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.translation import gettext as _
from .models import Post


def index(request):
    post_list = Post.objects.order_by('-title')
    return render(request, 'Blog/page.html', {'post_list': post_list})


def detail(request, post_uuid):
    try:
        uuid = Post.objects.get(uuid=post_uuid)
    except:
        raise Http404('Статья не найдена!')
    return render(request, 'Blog/page-detail.html', {'uuid':uuid})


def django(request):
    # Translators: This message appears on the django page only
    a = _('Django is perfect')
    return HttpResponse(a)
