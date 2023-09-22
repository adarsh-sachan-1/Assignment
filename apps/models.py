from django.db import models

# Create your models here.


class Article(models.Model):
    """
    Create database table and field using this model
    """
    pmid = models.CharField(primary_key=True, max_length=20)
    title = models.TextField()
    abstract = models.TextField()
    keywords = models.TextField()
    full_text_link = models.URLField()

    def __str__(self):
        return self.title
