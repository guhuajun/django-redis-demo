# -*- coding: utf-8 -*-
# pylint: disable=

import names

from django.views.generic.base import TemplateView


class PeopleView(TemplateView):

    template_name = 'people.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['names'] = [names.get_full_name() for x in range(100)]
        return context