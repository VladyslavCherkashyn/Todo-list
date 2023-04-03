from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True, unique=True)

    class Meta:

        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", default="General")

    class Meta:
        ordering = ["-created"]
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return (
            f" -> content: {self.content},"
            f" deadline: {self.deadline},"
            f" status: {self.is_completed},"
            f" type: {self.tags.name}"
        )
