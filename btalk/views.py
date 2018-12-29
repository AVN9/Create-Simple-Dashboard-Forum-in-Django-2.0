from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from btalk.models import Board, Topic, Post
from btalk.forms import NewTopicForm

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        #user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return HttpResponseRedirect(reverse('board_topics', kwargs={'pk': board.pk}))
            #return redirect('board_topics', pk=board.pk)
    else:
        #form = NewTopicForm()
        return render(request, 'new_topic.html', {'board': board})