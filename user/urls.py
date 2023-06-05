"""
# http://127.0.0.1:8000/user
# 1. /user로 요청이들어오면 <project>/urls.py 로 접근하여 일치하는 url을 찾는다.
# 2. 일치하는 url이 있으면 타고 들어간다. (include일 경우에는 해당하는 urls.py로 들어가서 2번 반복 
     또는 viewFunction일 경우 해당하는 viewFunction을 실행시킨다.)
# 3. viewFunction에서는 request를 받아 response를 반환한다.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_profile),
]