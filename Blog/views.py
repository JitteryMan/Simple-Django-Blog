from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'Blog/page.html')


def django(request):
    # Translators: This message appears on the django page only
    a = _('Django is perfect')
    return HttpResponse(a)
