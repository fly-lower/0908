from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='')
    name = models.CharField(max_length=32,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    height = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='身高')
    birthday = models.DateField(verbose_name='生日')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
