from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import Message
from .services.bot import handle_message
from .services.info import checkin
from .services.sort import sort_start
from .services.consultation import consultation


class MessageViewset(APIView):
    """
    Receive Bot messages.
    """

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        handle_message(request.POST)
        
        return Response('Message received')


class InfoView(APIView):
    """
    Get info and mark checkin.
    """

    def post(self, request, session_id):
        """
        Return mark checkin as done and get data.
        """
        res = checkin(session_id, post=True)
        return Response(res)

    def get(self, request, session_id):
        """
        Return mark checkin as done and get data.
        """
        res = checkin()
        return Response(res)


class SortingView(APIView):

    def get(self, request, session_id=None):
        res = sort_start()
        return Response(res)

    def post(self, request, session_id):
        """
        Post sorting timestamp
        """
        res = sort_start(int(session_id))
        return Response(res)


class ConsultationView(APIView):

    def post(self, request, session_id, start):
        """
        Post sorting timestamp
        """
        res = consultation(session_id, start)
        return Response(res)