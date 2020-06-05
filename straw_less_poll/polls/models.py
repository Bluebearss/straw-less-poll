from django.db import models


# Question Model that consists of a Question Textfield (max length 250) and a Publish Date
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    publish_date = models.DateTimeField('Date Published')

    # String format definition of a Question Model
    def __str__(self):
        return self.question_text


# Choice Model that consists of a Question Model (so Choice is linked to the Question it is for), Choice Textfield
# (max length 250), and a Votes integer.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    # String format definition of a Choice Model
    def __str__(self):
        return self.choice_text
