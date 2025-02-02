"""resumebuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from builder import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('',views.IndexListView.as_view(),name='index'),
    path('<int:pk>/',views.ResumeTemplateDetailView.as_view(),name='detail'),
    path('create/<int:pk>/',views.ResumeCreateView.as_view(),name='create'),
    path('<slug:slug>/',views.ResumeReadyView.as_view(), name='resumedwnbtn'),
    path('download/<slug:slug>/',views.DownloadView.as_view(), name='download'),


    # path('1/<int:pk>/',views.MyModelView.as_view(), name='h1'),
    # path('2',views.CustomWeasyTemplateResponse.as_view(), name='h2'),
    # path('3/<int:pk>/',views.MyModelPrintView.as_view(), name='h3'),
    # path('4/<int:pk>/',views.MyModelDownloadView.as_view(), name='h4'),
    # path('5/<int:pk>/',views.MyModelImageView.as_view(), name='h5'),

]
