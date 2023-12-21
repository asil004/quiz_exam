from random import shuffle, sample

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.cache import cache
from .filters import ResultFilter
from .models import Question, Result, QuizType
from .utils import check_answer
from django_filters.views import FilterView

User = get_user_model()


def qiuz(request):
    quizs = QuizType.objects.all()
    context = {
        'quizs': quizs
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def question(request, pk):
    questions = Question.objects.filter(quiz_id=pk)
    if questions.count() > 5:
        questions = sample(list(questions), 5)
    else:
        questions = sample(list(questions), questions.count())
    if request.method == "POST":
        context = check_answer(request)
        cache.delete('questions')
        return render(request, 'quizapp/result.html', context)

    if not cache.get('questions'):
        cache.set('questions', questions, timeout=360)
    questions = cache.get('questions')
    context = {
        'questions': questions,
    }
    return render(request, 'quizapp/question.html', context)


# def result_list(request):
#     results = Result.objects.all()
#     filter = ResultFilter
#     context = {
#         'results': results
#     }
#     return render(request, 'quizapp/result_list.html', context)

class ResultList(FilterView):
    model = Result
    queryset = Result.objects.all()
    filterset_class = ResultFilter
    context_object_name = 'result'
    template_name = 'quizapp/result_list.html'
