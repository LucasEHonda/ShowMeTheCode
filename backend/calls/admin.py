from django.contrib import admin

from calls.models import Call


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ["user", "origin", "destiny", "plan", "minutes"]
    search_fields = ["user", "origin", "destiny", "plan"]
    list_filter = [
        "user",
        "plan",
        "origin",
        "destiny",
    ]
