"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.forms import QuestionForm
from app.models import *
from app.utils import AppUtils
from django.views.generic.detail import DetailView


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
        utils = AppUtils()
        question = utils.create_question(form.data['title'], form.data['body'], UserExtension.objects.get(pk = 1))
        return HttpResponseRedirect('/question/' + str(question.id))


class QuestionDetailView(DetailView):
    """Renders the question details page."""
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Question'
        context['year'] = datetime.now().year
        return context