from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
#모델을 정의하는 코드(여기서 모델의 이름은 Post), models.Model로 db에 인식됨
    author=models.ForeignKey('auth.User')
    #다른 모델에 대한 링크
    title=models.CharField(max_length=200)
    #글자 수가 제한된 텍스트(글제목같은느낌)
    text=models.TextField()
    #글자 수에 제한이 없는 텍스트
    create_date=models.DateTimeField(
            default=timezone.now)#날짜와시간
    published_date=models.DateTimeField(
            blank=True,null=True)

    def publish(self):
        #메서드!
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
