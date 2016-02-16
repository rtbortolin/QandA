from app.models import Question, QuestionComment, Answer, AnswerComment, QuestionVote, AnswerVote

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
        question.save()
        return comment
    
    def make_a_answer(self, body, question_id, user):
        question = Question.objects.get(pk = question_id)
        answer = Answer()
        answer.question = question;
        answer.body = body
        answer.creator = user
        answer.updater = user
        answer.is_accepted = False
        answer.save()
        question.save()
        return answer

    def vote(self, question_id, vote_type, user):
        question = Question.objects.get(pk = question_id)
        vote = QuestionVote()
        vote.grade = vote_type
        vote.question = question
        vote.voter = user
        question.save()
        vote.save()

class AnswerServices(object):
    
    def create_comment(self, comment_text, question_id, answer_id, user):
        question = Question.objects.get(pk = question_id)
        answer = Answer.objects.get(pk = answer_id)
        comment = AnswerComment()
        comment.text = comment_text;
        comment.answer = answer
        comment.app_user = user
        comment.save()
        question.save()
        return comment

    def vote(self, question_id, answer_id, vote_type, user):
        answer = Answer.objects.get(pk = answer_id)
        question = Question.objects.get(pk = question_id)
        vote = AnswerVote()
        vote.grade = vote_type
        vote.answer = answer
        vote.voter = user
        question.save()
        vote.save()


