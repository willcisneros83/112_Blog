from django.test import SimpleTestCase
from django.urls import reverse


class PagesTests(SimpleTestCase):

    def test_home_page_view_is_up(self):
        response = self.client.get("/pages/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_is_up(self):
        response = self.client.get("/pages/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_uses_correct_templates(self):
        response = self.client.get("/pages/")
        self.assertTemplateUsed(response, "pages_templates/home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_view_uses_correct_templates(self):
        response = self.client.get("/pages/about/")
        self.assertTemplateUsed(response, "pages_templates/about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_view_has_correct_content(self):
        response = self.client.get("/pages/")
        self.assertContains(response, "This is home")

    def test_about_page_view_has_correct_content(self):
        response = self.client.get("/about/")
        self.assertContains(response, "Hey this is my about page")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status.code, 200)
        self.assertTemplateUsed(response, "pages/home.html")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status.code, 200)
        self.assertTemplateUsed(response, "pages/about.html")

    
        
        


