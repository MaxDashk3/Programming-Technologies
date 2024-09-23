import unittest
from unittest import expectedFailure

import NewsQueue as app

class TestNewsQueue(unittest.TestCase):
    #sets up news queue before each test
    def setUp(self):
        self.queue = [app.News("Title 1", "Content 1"),
                      app.News("Title 2", "Content 2"),
                      app.News("Title 3", "Content 3")]

    #tests if addition works correctly and if an error raises when adding an empty item
    def test_add(self):
        app.add("Title 4", "Content 4", self.queue)
        self.assertEqual(self.queue[3].title, "Title 4")
        self.assertEqual(self.queue[3].content, "Content 4")
        self.assertRaises(ValueError, app.add, '', '', self.queue)

    #checks if pop changes size of queue and it's contents
    def test_pop(self):
        init_len = len(self.queue)
        app.pop(self.queue)
        self.assertEqual(len(self.queue), init_len - 1)
        self.assertEqual(self.queue[0].title, "Title 2")

    #checks if exception is raised if queue is empty
    def test_view(self):
        self.queue=[]
        self.assertRaises(ValueError, app.view_all, self.queue)

    #checks if searching by title works correctly
    def test_title_index(self):
        self.assertEqual(app.title_index("Title 2", self.queue), 1)
        self.assertEqual(app.title_index("Bad title", self.queue), -1)

    #checks if retrieving news item by title works correctly
    def test_news_by_title(self):
        news = app.news_by_title("Title 2", self.queue)
        self.assertEqual(news.content, "Content 2")
        self.assertRaises(ValueError, app.news_by_title, "Bad title", self.queue)

    #causes a test failure
    @expectedFailure
    def test_fail(self):
        init_len=len(self.queue)
        app.pop(self.queue)
        self.assertEqual(len(self.queue), init_len)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
