from django.urls import path


from todomanager.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskDeleteView,
    TaskDoneView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("<int:pk>", TaskDoneView.as_view(), name="task_done"),
    path("tag/", TagListView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path('tag/<int:pk>/edit/', TagUpdateView.as_view(), name="tag_edit"),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "todomanager"
