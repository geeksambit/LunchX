from django.db import models

from users.models import User

# Create your models here.


class Quiz(models.Model):
    name = models.CharField(verbose_name='Name', max_length=52, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def question(self):
        return self.question_set.all()



class Question(models.Model):
    question = models.CharField(verbose_name='Name', max_length=2000)
    option1 = models.CharField(verbose_name='option1', max_length=500)
    option2 = models.CharField(verbose_name='option2', max_length=500)
    option3 = models.CharField(verbose_name='option3', max_length=500)
    option4 = models.CharField(verbose_name='option4', max_length=500)
    ans = models.CharField(verbose_name='ans', max_length=500)
    quiz =models.ForeignKey(Quiz,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.question)




class Test(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qiiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    attained = models.IntegerField()
    not_attained = models.IntegerField()
    correct = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)