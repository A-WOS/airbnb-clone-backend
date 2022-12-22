from .models import Category
from django.http import JsonResponse
from django.core import serializers


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "ok": True,
            # serializers = querySet 을 json 타입으로 변경
            "categories": serializers.serialize("json", all_categories),
        }
    )
