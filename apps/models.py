from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Books(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    create_at=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

