from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(verbose_name='Name', max_length=52, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)


class Subject(models.Model):
    name = models.CharField(verbose_name='Name', max_length=52, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)





