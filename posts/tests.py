from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class PostsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "Testuser",
            "test@test.com"
        )
        self.post = Post.objects.create(
            title = "My post",
            author = self.author,
            body = "Test"
        )

    def test_post_model_string_representation(self):
        self.assertEqual(str(self.post), "My post")

    def test_post_model_content(self):
        self.assertEqual(f"{self.post.title}", "My post")
        self.assertEqual(f"{self.post.body}", "Test")
        self.assertEqual(f"{self.post.author}", "Testuser")

    def test_post_list_view_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_content(self):
        response = self.client.get(reverse(post_list))
        self.assertContains(response, "My post")
        self.assertContains(response, "By: Testuser")
        self.assertContains(response, "Test")
    
    def test_post_detail_view_status_code(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_create_view_status_code(self):
        response = self.client.get("/posts/new/")
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view_status_code(self):
        response = self.client.get("/posts/1/delete/")
        self.assertEqual(response.status_code, 302)

    def test_post_edit_view_status_code(self):
        response = self.client.get("/posts/1/edit/")
        self.assertEqual(response.status_code, 302)



