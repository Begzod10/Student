from django.urls import path

from users.comments.api import CommentCreateView, CommentListView

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('list/', CommentListView.as_view(), name='comment-list'),
]
