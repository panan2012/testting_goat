from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page  

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

       
    def test_can_save_a_POST_request(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertContains(response, "A new list item")
        self.assertTemplateUsed(response, "home.html")

        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode("utf8")
        # self.assertIn("<title>To-Do lists</title>", html)
        # self.assertTrue(html.startswith("<html>"))
        # self.assertTrue(html.endswith("</html>"))

    # def test_home_page_returns_correct_html_2(self):
    #     response = self.client.get("/")
    #     self.assertContains(response, "<title>To-Do lists</title>")


    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')  
    #     self.assertEqual(found.func, home_page)  
    