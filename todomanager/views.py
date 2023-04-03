from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone

from todomanager.forms import TaskForm, TagForm
from todomanager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todomanager/task_list.html"

    def get_queryset(self):
        return Task.objects.filter(deadline__gte=timezone.now()).order_by("-created")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todomanager/task_form.html"
    success_url = reverse_lazy("todomanager:task_list")

    def form_valid(self, form):
        form.instance.created = timezone.now()
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todomanager/task_form.html"
    success_url = reverse_lazy("todomanager:task_list")

    def form_valid(self, form):
        form.instance.created = timezone.now()
        return super().form_valid(form)


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todomanager/task_confirm_delete.html"
    success_url = reverse_lazy("todomanager:task_list")


class TaskDoneView(generic.UpdateView):
    model = Task
    fields = []
    success_url = reverse_lazy("todomanager:task_list")

    def form_valid(self, form):
        if form.instance.is_completed:
            form.instance.is_completed = False
        else:
            form.instance.is_completed = True
        form.instance.save()
        return super().form_valid(form)


class TagListView(generic.ListView):
    model = Tag
    template_name = "todomanager/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todomanager/tag_form.html"
    success_url = reverse_lazy("todomanager:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todomanager/tag_form.html"
    success_url = reverse_lazy("todomanager:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todomanager/tag_confirm_delete.html"
    success_url = reverse_lazy("todomanager:tag_list")

