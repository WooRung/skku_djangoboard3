from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from .models import Board, Comment
from .forms import BoardForm, CommentForm

def index(request):
    # 모델 - 데이터 조회하기 
    board_list = Board.objects.all()
    return render(request, 'board/index.html', {'board_list': board_list})


def board_detail(request, board_id):
    board = Board.objects.prefetch_related('comment_set').get(id=board_id)
    # comment_list = Comment.objects.filter(board_id=board_id).all()
    # comment_list = board.comment_set.all()
    
    # Comment Form 생성
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment(content=data['content'], board=board)
            comment.save()
            return redirect(reverse('board:detail', kwargs={'board_id': board_id}))

    return render(request, 'board/detail.html', {
            'board': board, 
            'form': form,
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

# 수정하기 view function
def board_edit(request, board_id):
    board = Board.objects.get(id=board_id)
    form = BoardForm(initial={
        'title': board.title,
        'content': board.content
    })
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['content']
            board.save()
            return redirect(reverse('board:detail', kwargs={'board_id': board_id}))

    return render(request, 'board/edit.html', {'form': form})