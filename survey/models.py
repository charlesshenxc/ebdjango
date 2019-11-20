from django.db import models
import uuid

# Create your models here.
class Survey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    user = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=300)
    kind = models.CharField(max_length=50, choices=(('radio', 'radio'), ('checkbox', 'checkbox')))

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.response
