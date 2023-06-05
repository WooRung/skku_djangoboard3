from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from .models import Board, Comment

def index(request):
    # 모델 - 데이터 조회하기 
    board_list = Board.objects.all()
    return render(request, 'board/index.html', {'board_list': board_list})


def board_detail(request, board_id):
    board = Board.objects.prefetch_related('comment_set').get(id=board_id)
    # comment_list = Comment.objects.filter(board_id=board_id).all()
    # comment_list = board.comment_set.all()
    return render(request, 'board/detail.html', {
        'board': board, 
        # 'comment_list': comment_list,
        })

def board_create(request):
    # print(dir(request))
    if request.method == 'POST':
        data = request.POST
        board = Board(
            title=data['title'],
            content=data['content']
        )
        board.save()
        return redirect(reverse('board:index'))
        # return redirect('/board')


        
    
    return render(request, 'board/create.html')