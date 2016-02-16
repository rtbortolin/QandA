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

def create_question(request):
    if request.method == "GET":
        form = QuestionForm()
        return render_to_response("app/questions/create.html", {'form':form},  RequestContext(request))
    elif request.method == 'POST':
        form = QuestionForm(request.POST)
        question_services = QuestionServices()
        question = question_services.create_question(form.data['title'], form.data['body'], UserExtension.objects.get(pk = 1))
        return HttpResponseRedirect('/question/' + str(question.id))

def make_question_comment(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        form = CommentForm(request.POST)
        question_service = QuestionServices()
        comment = question_service.create_comment(form.data['comment'], form.data['question_id'], UserExtension.objects.get(pk = 1))        
        return HttpResponseRedirect('/question/' + form.data['question_id'] + '?comment=' + str(comment.id))

def answer_a_question(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        question_service = QuestionServices()
        answer = question_service.make_a_answer(request.POST['body'], request.POST['question_id'], UserExtension.objects.get(pk = 1))        
        return HttpResponseRedirect('/question/' + request.POST['question_id'] + '?answer=' + str(answer.id))

def make_answer_comment(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        form = CommentForm(request.POST)
        answer_services = AnswerServices()
        comment = answer_services.create_comment(form.data['comment'], form.data['question_id'], form.data['answer_id'], UserExtension.objects.get(pk = 1))        
        return HttpResponseRedirect('/question/' + form.data['question_id'] + '?comment=' + str(comment.id) + '&answer=' + form.data['answer_id'])

def make_a_vote(request):
    if request.method == "GET":
        raise Http404
    if request.method == "POST":
        return HttpResponse('true', content_type="application/json")

class QuestionDetailView(DetailView):
    """Renders the question details page."""
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Question'
        context['year'] = datetime.now().year
        return context