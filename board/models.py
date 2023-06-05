from django.db import models

# Create your models here.
import importlib
# importlib.import_module('board.apps.BoardConfig')
from django.core import validators


class Board(models.Model):
    id = models.AutoField(primary_key=True)  # integer(auto-increment)
    title = models.CharField("제목", max_length=255,  # varchar(255)
                            validators=[
                                validators.MinLengthValidator(2, "최소 세 글자 이상은 입력해주셔야 합니다.")
                            ])
    content = models.TextField("내용", validators=[
        validators.MinLengthValidator(10, "최소 10글자 이상은 입력해주셔야 합니다."),
    ])  # Text
    created_at = models.DateTimeField(auto_now_add=True)  # 추가될 때 default로 현재시간
    updated_at = models.DateTimeField(auto_now=True)  # 추가or업데이트 될 때 default로 현재시간

    def __str__(self):
        return f"{self.id} - {self.title}"


class Comment(models.Model):
    # id = models.AutoField(primary_key=True)

    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    board = models.ForeignKey('Board',
                            #   related_name='comment_set',
                            on_delete=models.SET_NULL, null=True)
