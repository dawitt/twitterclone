from notification.models import Notification
from twitteruser.models import TweeterUser
from django.shortcuts import render, HttpResponseRedirect
from twitteruser import views
# Create your views here.

def notification_view(request):
    msg = Notification.objects.filter(is_seen=False).filter(notifier=request.user).order_by("-notification")
    return render(request, 'notification.html', {'msg':msg})

def delete_notification(request, id):
    note = Notification.objects.get(id=id)
    note.is_seen = True
    note.save()
    return HttpResponseRedirect("/notification/")