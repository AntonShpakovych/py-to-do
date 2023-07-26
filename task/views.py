from django.shortcuts import render

from task.models import Task


def home_page(request):
    tasks = Task.objects.prefetch_related("tags")

    context = {
        "tasks": tasks
    }
    return render(request, "task/index.html", context=context)
