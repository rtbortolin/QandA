from app.models import Question

class AppUtils(object):
    """description of class"""
    
    def create_question(self, title, body, user):
        question = Question()
        question.title = title
        question.body = body
        question.creator = user
        question.updater = user
        question.save()
        return question
