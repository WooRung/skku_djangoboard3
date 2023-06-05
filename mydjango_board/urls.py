"""mydjango_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
# http://127.0.0.1:8000/user
# 1. /user로 요청이들어오면 <project>/urls.py 로 접근하여 일치하는 url을 찾는다.
# 2. 일치하는 url이 있으면 타고 들어간다. (include일 경우에는 해당하는 urls.py로 들어가서 2번 반복 
     또는 viewFunction일 경우 해당하는 viewFunction을 실행시킨다.)
# 3. viewFunction에서는 request를 받아 response를 반환한다.
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path('board/', include('board.urls')),
    path('user/', include('user.urls')),
]
