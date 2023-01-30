from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDitail.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments')
               ]