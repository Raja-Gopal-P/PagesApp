from django.shortcuts import redirect, render
from django.shortcuts import reverse
from django.views.generic import DetailView

import re

from .models import Page


def index_view(request):
    return redirect(reverse('Pages:target_page', kwargs={'title_slug': 'home'}))


class PageView(DetailView):

    template_name = 'Pages/page_view.html'
    queryset = Page.objects.order_by('ordering')
    slug_url_kwarg = 'title_slug'

    context_object_name = 'current_page'

    def get_context_data(self, **kwargs):
        kwargs['pages'] = self.get_queryset()
        return super().get_context_data(**kwargs)


def reorder_page(request,**kwargs):
    context = {}
    page_order_dict = {}
    if request.method == 'POST' and request.user.is_superuser:
        items_order = request.POST.get('items_order')
        ordered_pages = items_order.split('&')

        for order, page in enumerate(ordered_pages):
            if re.match(r'^(item\[\]=\d+)$', page):
                page_id = int(page.split('=')[1])
                page_order_dict[page_id] = order
            else:
                context['op_fail'] = 'Order Change Request Failed. Retry!!'
                page_order_dict = {}
                break

    if page_order_dict:
        try:
            pages = Page.objects.all()
            for page in pages:
                page.ordering = page_order_dict[page.id]
                page.save()
        except:
            context['op_fail'] = 'Order Change Request Failed. Retry!!'
        else:
            return redirect(reverse('Pages:index'))

    pages = Page.objects.order_by('ordering')
    context['pages'] = pages
    return render(request, 'Pages/reorder.html', context)
