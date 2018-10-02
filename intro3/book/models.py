import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

def __str__(self):
    return ("ID: %s, Question: %s" %(self.id, self.question_text))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return ("ID: %s, Choice: %s" %(self.id, self.choice_text))

class Book(models.Model):
    name= models.CharField(max_length=200)
    stars=models.CharField(max_length=200)
    release_Date=models.CharField(max_length=200)
    current_Date=models.DateTimeField('current date')
    def __str__(self):
        return ("The name of the book is: %s. It's rated: %s stars, and was released in %s"
                %(self.name, self.stars, self.release_Date))