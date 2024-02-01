from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ChatHistory
from django.contrib.auth.decorators import login_required

# Create your views here.
class Chat(TemplateView):
    template_name = 'chat.html'

@login_required
def room(request, roomID):
    userID = request.user.username
    allMessages = ChatHistory.objects.all().filter(sendRoom__exact=roomID)

    return render(request, "room.html", {"roomID": roomID, "allMessage": allMessages, "user": userID})