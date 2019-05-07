# -*- coding: utf-8 -*-
# pylint: disable=

from django.urls import re_path
from django.views.decorators.cache import cache_page


from people import views

urlpatterns = [
    re_path('^', cache_page(10)(views.PeopleView.as_view()), name='people')
]