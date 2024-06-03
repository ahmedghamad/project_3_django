from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"The title of this post is {self.book_title}"
