from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.db.models import Max, Count
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import Survey, Question, Choice, Response

import re

# Create your views here.
@login_required
def index(request):
    user = request.user.username
    survey_list = Survey.objects.filter(user=user)
    context = {
        'survey_list': survey_list
    }
    return render(request, 'index.html', context)

@login_required
def create_survey(request):
    if request.method == "POST":
        survey_title = request.POST.get('survey_title', '')
        survey_description = request.POST.get('survey_description', '')
        user = request.user.username
        survey = Survey(title=survey_title, description=survey_description, user=user)
        survey.save()
        survey_id = survey.id
        return HttpResponseRedirect(reverse('create_question', args=[survey_id]))
    else:
        return render(request, 'create_survey.html')

@login_required
def create_question(request, survey_id):
    if request.method == "POST":
        question_number = request.POST.get('question_number', '')
        question_title = request.POST.get('question_title', '')
        question_type = request.POST.get('question_type', '')
        question = Question(
            number = question_number,
            title = question_title,
            kind = question_type,
            survey = Survey.objects.get(id=survey_id)
        )
        question.save()
        if question_type in ['radio', 'checkbox']:
            question_id = question.id
            choice_list = request.POST.getlist('choice_title')
            for choice_title in choice_list:
                choice = Choice(
                    title = choice_title,
                    question = Question.objects.get(id=question_id)
                )
                choice.save()
        return HttpResponseRedirect(reverse('create_question', args=[survey_id]))
    else:
        survey = get_object_or_404(Survey, pk=survey_id)
        question_number_max_dict = Question.objects.filter(survey=survey_id).aggregate(Max('number'))
        question_number_max = question_number_max_dict.get('number__max')
        if question_number_max:
            question_number = question_number_max + 1
        else:
            question_number = 1
        context = {
            'survey': survey,
            'question_number': question_number
        }
        return render(request, 'create_question.html', context)

@login_required
def delete_survey(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    survey.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def result(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    response_list = Response.objects.filter(
        question__survey=survey_id
    ).order_by('question__number').values(
        'question__title',
        'response'
    ).annotate(num_response=Count('response'))
    context = {
        'survey': survey,
        'response_list': response_list
    }
    return render(request, 'result.html', context)

def survey(request, survey_id):
    if request.method == "POST":
        for key, value in request.POST.items():
            if 'q_checkbox' in key or 'q_radio' in key:
                question_id = re.sub(r'\D', '', key)
                response_text = value
                if 'q_checkbox' in key:
                    response_text = request.POST.getlist(key)
                if question_id and response_text:
                    response = Response(
                        response = response_text,
                        date = timezone.now(),
                        question = Question.objects.get(id=question_id)
                    )
                    response.save()
        return HttpResponseRedirect(reverse('complete'))
    else:
        survey = get_object_or_404(Survey, pk=survey_id)
        context = {'survey': survey}
        return render(request, 'survey.html', context)

def complete(request):
    return render(request, 'complete.html')

def login(request):
    if request.method == "POST":
        next_url = request.POST.get('next', '/')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            context = {
                'password_is_wrong': True
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")