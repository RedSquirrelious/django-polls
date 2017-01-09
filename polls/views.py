from django.shortcuts import render

from django.http import HttpResponse, Http404



from .models import Question, Choice

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list,}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	else:
		return render(request, 'polls/detail.html', {'question': question})
	# return HttpResponse("This is the detail view of the question: %s" % question_id)

def results(request, question_id):
	return HttpResponse("These are the results of the question: %s" % question_id)
	# return render("These are the results of the question: %s" % question_id)

def vote(request, question_id):
	return	HttpResponse("Vote on question: %s" % question_id)
	# return	render("Vote on question: %s" % question_id)