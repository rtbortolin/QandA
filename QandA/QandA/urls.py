"""
Definition of urls for QandA.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
import app
import app.views
import django.contrib.auth.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^question/create$', app.views.create_question, name = "create_question"),
    url(r'^question/(?P<pk>\d+)$', app.views.QuestionDetailView.as_view(template_name='app/questions/details.html'), name = "Question Detail"),

    url(r'^question/comment$', app.views.make_question_comment, name = "make_question_comment"),
    url(r'^question/answer$', app.views.answer_a_question, name = "answer_a_question"),
    url(r'^question/answer/comment$', app.views.make_answer_comment, name = "make_answer_comment"),
    url(r'^question/vote$', app.views.make_a_vote, name = "make_a_vote"),
        #url(r'^$', HomePageView.as_view(), name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
