from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BaseEntity(models.Model):
    created_in = models.DateTimeField(auto_now_add = True)
    updated_in = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = False)

    class Meta:
        abstract = True

class UserExtension(BaseEntity):
    user = models.OneToOneField(User, primary_key = True)
    points = models.IntegerField(default = 0)

class Post(BaseEntity):
    body = models.TextField()

    def days_since_post(self):
        timediff =  timezone.now() - self.created_in 
        return timediff.days

    class Meta:
        abstract = True

class Vote(BaseEntity):
    GRADE_VALUES = (
        ("P", "Positive"),
        ("N", "Negative"),
    )
    voter = models.OneToOneField(UserExtension)
    grade = models.CharField(max_length = 1, choices = GRADE_VALUES)

    class Meta:
        abstract = True

class Question(Post):
    title = models.CharField(max_length = 255)
    creator = models.ForeignKey(UserExtension, related_name = "questions_created")
    updater = models.ForeignKey(UserExtension, related_name = "questions_updated")

class Answer(Post):
    question = models.ForeignKey(Question)
    is_accepted = models.BooleanField()
    creator = models.ForeignKey(UserExtension, related_name = "answer_created")
    updater = models.ForeignKey(UserExtension, related_name = "answer_updated")

class AnswerVote(Vote):
    answer = models.ForeignKey(Answer)

class QuestionVote(Vote):
    question = models.ForeignKey(Question)


class Tag(BaseEntity):
    name = models.CharField(max_length = 25)
    questions = models.ManyToManyField(Question)

class Comment(BaseEntity):
    text = models.CharField(max_length = 500)
    app_user = models.ForeignKey(UserExtension)

    class Meta: 
        abstract = True

class QuestionComment(Comment):
    question = models.ForeignKey(Question)

class AnswerComment(Comment):
    answer = models.ForeignKey(Answer)