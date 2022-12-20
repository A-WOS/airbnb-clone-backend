from django.contrib import admin

from reviews.models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("thanks", "Thanks"),
            ("awesome", "Awesome"),
            ("별로", " 별로"),
        ]

    def queryset(self, request, reviews):
        # print(request.GET['word']) == print(self.value)
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pets_friendly",
    )
