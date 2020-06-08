from django.shortcuts import render
from .models import Question, Choice


# Get Questions from data and display them.
def index(request):
    curr_question_list = Question.objects.order_by('-publish_date')[:5]
    context = {'curr_question_list': curr_question_list}
    return render(request, 'polls/index.html', context)


# Show specific Question and Choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/results.html', {'question': question})
