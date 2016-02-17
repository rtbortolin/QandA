"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.forms import QuestionForm, CommentForm
from app.models import *
from app.utils import QuestionServices, AnswerServices
from django.views.generic.detail import DetailView
from django.http.response import Http404
from django.contrib.auth.decorators import login_required, REDIRECT_FIELD_NAME
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

@login_required()
def make_question_comment(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        form = CommentForm(request.POST)
        user = request.user.userprofile

        question_service = QuestionServices()
        comment = question_service.create_comment(form.data['comment'], form.data['question_id'], user)        
        return HttpResponseRedirect('/question/' + form.data['question_id'] + '?comment=' + str(comment.id))

@login_required()
def answer_a_question(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        user = request.user.userprofile

        question_service = QuestionServices()
        answer = question_service.make_a_answer(request.POST['body'], request.POST['question_id'], user)        
        return HttpResponseRedirect('/question/' + request.POST['question_id'] + '?answer=' + str(answer.id))

@login_required()
def make_answer_comment(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        form = CommentForm(request.POST)
        user = request.user.userprofile

        answer_services = AnswerServices()
        comment = answer_services.create_comment(form.data['comment'], form.data['question_id'], form.data['answer_id'], user)        
        return HttpResponseRedirect('/question/' + form.data['question_id'] + '?comment=' + str(comment.id) + '&answer=' + form.data['answer_id'])

@login_required()   
def make_a_vote(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        question_id = request.POST['question_id']
        answer_id = request.POST['answer_id']
        vote_for = request.POST['votefor']
        vote_type = request.POST['vote_type']

        vote_type = 'P' if vote_type == 'like' else 'N'

        user = request.user.userprofile
           
        if(answer_id == '' and vote_for == 'answer'):
            raise Http404

        if(vote_for == 'question'):
            question_utils = QuestionServices()
            question_utils.vote(question_id, vote_type, user)
            return HttpResponse('true', content_type="application/json")
        elif (vote_for == 'answer'):
            answer_utils = AnswerServices()
            answer_utils.vote(question_id, answer_id, vote_type, user) 
            return HttpResponse('true', content_type="application/json")
        else :
            return HttpResponse('false', content_type="application/json")
       
@login_required()                    
def create_question(request):
    if request.method == "GET":
        form = QuestionForm()
        return render_to_response("app/questions/create.html", {'form':form},  RequestContext(request,{ 'title': 'Create new question' }))
    elif request.method == 'POST':
        user = request.user.userprofile

        form = QuestionForm(request.POST)
        question_services = QuestionServices()
        question = question_services.create_question(form.data['title'], form.data['body'], user)
        return HttpResponseRedirect('/question/' + str(question.id))


class QuestionDetailView(LoginRequiredMixin, DetailView):
    """Renders the question details page."""
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Question'
        context['year'] = datetime.now().year
        return context