from django.db import models


class CommonModel(models.Model):
    """ Common Model Definition """

    # DateTimeField -> 년, 날짜, 요일, 시, 분, 초
    # DateField -> 날짜, 달, 년 만 저장.

    # auto_now_add -> 처음 생성한 날짜 저장
    # update 될 때마다 날짜 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # db에 모델이 생성 되지 않고 다른 모델들이 상속을 받을 수 있도록 해줌
        abstract = True
