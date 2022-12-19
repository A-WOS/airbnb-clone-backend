from django.db import models


class CommonModel(models.Model):
    """ Common Model Definition """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # db에 모델이 생성 되지 않고 다른 모델들이 상속을 받을 수 있도록 해줌
        abstract = True
