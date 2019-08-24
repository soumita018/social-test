from django.db import models

# Create your models here.

class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
