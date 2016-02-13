from app.models import Question, QuestionComment

class QuestionServices(object):

        def create_question(self, title, body, user):
            question = Question()
            question.title = title
            question.body = body
            question.creator = user
            question.updater = user
            question.save()
            return question

        def create_comment(self, comment_text, question_id, user):
            question = Question.objects.get(pk = question_id)
            comment = QuestionComment()
            comment.text = comment_text;
            comment.question = question
            comment.app_user = user
            comment.save()
            return comment
