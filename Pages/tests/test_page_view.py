from django.test import TestCase
from ..models import Page
from django.shortcuts import reverse


class PageViewTests(TestCase):

    def setUp(self):
        self.page1 = Page.objects.create(title='home', slug='home', content_html='<p>Hi</p>All')
        self.page2 = Page.objects.create(title='about', slug='about', content_html='<p>Welcome</p>All')
        self.response = self.client.get(reverse('Pages:target_page', kwargs={'title_slug': self.page2.slug}))

    def test_home_redirect(self):
        response = self.client.get(reverse('Pages:index'))
        self.assertRedirects(response, reverse('Pages:target_page', kwargs={'title_slug': 'home'}))

    def test_required_context_objects(self):
        page = self.response.context.get('current_page')
        pages = self.response.context.get('pages')
        self.assertTrue(page)
        self.assertTrue(pages)

    def test_ui_response(self):
        self.assertContains(self.response, '/{}/'.format(self.page1.slug))
        self.assertContains(self.response, '/{}/'.format(self.page2.slug))
        self.assertContains(self.response, self.page2.content_html)

    def test_404(self):
        response = self.client.get(reverse('Pages:target_page', kwargs={'title_slug': 'none'}))
        self.assertEqual(response.status_code, 404)
