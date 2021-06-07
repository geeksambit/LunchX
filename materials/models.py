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

        

class StudyMaterial(models.Model):
    name = models.CharField(verbose_name='Name', max_length=52, unique=True)
    subject =models.ForeignKey(Subject,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return '{}'.format(self.name)







