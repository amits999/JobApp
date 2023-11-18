from django.urls import path
from app import views

urlpatterns = [
    path('', views.hello, name='main_page'),
    path('job/<int:id>', views.job_detail_page, name='jobs_detail')
]