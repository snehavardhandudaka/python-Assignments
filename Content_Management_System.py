# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)  # Title of the article
    content = models.TextField()  # Main content of the article
    published_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the article is created

    def __str__(self):
        return self.title  # Return the title when an Article instance is printed

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-published_date']  # Order by published_date in descending order

    # Additional method example
    def summary(self):
        return self.content[:100]  # Return the first 100 characters of the content
