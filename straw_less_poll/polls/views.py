from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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
    return render(request, 'polls/detail.html', {'question': question})


# Get question and display its results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# Vote for a question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay form of questions to vote from.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Choice not selected.",
        })
    else:
        choice.votes += 1
        choice.save()

        # Always return HttpResponseRedirect after successfully dealing with POST data. Prevents data being posted twice
        # w/ user Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
