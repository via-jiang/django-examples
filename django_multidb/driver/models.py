from django.db import models


# Create your models here.
class Driver(models.Model):

    class Meta:
        db_table = 'Driver'

    name = models.CharField('司机姓名', max_length=12)
    age = models.IntegerField('司机年龄')
