from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from .models import Board, Comment
from .forms import BoardForm

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
    form = BoardForm()

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # board = Board(
            #     title=data['title'],
            #     content=data['content']
            # )
            # board.save()
            form.save(commit=True)
            return redirect(reverse('board:index'))
            # return redirect('/board')


        
    
    return render(request, 'board/create.html', {'form': form})