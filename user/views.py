"""
# http://127.0.0.1:8000/user
# 1. /user로 요청이들어오면 <project>/urls.py 로 접근하여 일치하는 url을 찾는다.
# 2. 일치하는 url이 있으면 타고 들어간다. (include일 경우에는 해당하는 urls.py로 들어가서 2번 반복 
     또는 viewFunction일 경우 해당하는 viewFunction을 실행시킨다.)
# 3. viewFunction에서는 request를 받아 response를 반환한다.
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from django.contrib.auth import models

# from django.conf import settings
from .forms import RegisterForm

from django.contrib.auth import authenticate, login


def index(request):
  print(request.user)
  print(request.user.is_authenticated)
  print(request.user.is_superuser)
  print(request.user.is_staff)
  return render(request, 'user/profile.html')

def register(request):
  form = RegisterForm()
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      print(username)
      print(password)
      user = authenticate(username=username, password=password) # DB의 유저정보와 비교 및 조회
      login(request, user) # 실질적인 로그인
      return redirect(reverse('user:index'))

  return render(request, 'user/register.html', {'form': form})

# class SampleView(View):
#   def get(self, request, *args, **kwargs):
#     return HttpResponse('get요청')
#   def post(self, request, *args, **kwargs):
#     return HttpResponse('post요청')
    
#   def put(self, request, *args, **kwargs):
#     return HttpResponse('put요청')

#   def delete(self, request, *args, **kwargs):
#     return HttpResponse('delete요청')

# def user_profile(request):
#     return HttpResponse(
#       """
#       <h1>나의 프로필</h1>
#       <ul>
#         <li>이름: 신윤수</li>
#         <li>별명: ys</li>
#       </ul>
#       """
#     )