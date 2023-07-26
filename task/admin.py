from django.contrib import admin

from task.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        "created_at", "deadline", "is_completed"
    )

    list_filter = ("is_completed", "deadline")


admin.site.register(Tag)
