from django.http import HttpResponse
from django.shortcuts import render

from .models import Board

def index(request):
    # 모델 - 데이터 조회하기 
    board_list = Board.objects.all()

    return render(request, 'board/index.html', {'board_list': board_list})


def board_detail(request, board_id):
    board = Board.objects.prefetch_related('comment_set').get(id=board_id)
    return render(request, 'board/detail.html', {'board': board})