from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

app_name = "courses"

urlpatterns = [
    path('admin/', admin.site.urls),

    #url(r'^couses/')
    #path('', views.SnippetListView.as_view(), name='list'),
    #path('<int:pk>/', views.SnippetDetailView.as_view(), name='detail')
]