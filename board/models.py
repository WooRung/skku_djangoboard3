from django.db import models

# Create your models here.


class Board(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.title}"


class Comment(models.Model):
    # id = models.AutoField(primary_key=True)

    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    board = models.ForeignKey('Board', related_name='comment_set',
                              on_delete=models.SET_NULL, null=True)
