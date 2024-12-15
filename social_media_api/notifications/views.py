from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, is_read=False)
        notifications_data = [{"actor": n.actor.username, "verb": n.verb, "target": str(n.target), "timestamp": n.timestamp} for n in notifications]
        return Response({"notifications": notifications_data}, status=200)
