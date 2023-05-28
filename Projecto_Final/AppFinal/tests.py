from django.test import TestCase
from.models import BlogPost

class BlogPostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BlogPost.objects.create(title='Test Post', subtitle='Test Subtitle', content='Test Content', category='Test Category')

    def test_title_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('title').max_length
        self.assertEqual(max_length, 300)

    def test_subtitle_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('subtitle').verbose_name
        self.assertEqual(field_label, 'subtitle')

    def test_subtitle_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('subtitle').max_length
        self.assertEqual(max_length, 900)

    def test_content_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_content_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('content').max_length
        self.assertEqual(max_length, 10000)

    def test_category_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_category_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('category').max_length
        self.assertEqual(max_length, 45)