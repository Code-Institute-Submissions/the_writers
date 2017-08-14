from django.test import TestCase
from .models import Post


class PostTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post model
    """

    def test_str(self):
        test_title = Post(title='Testing the title')
        self.assertEqual(str(test_title),
                         'Testing the title')