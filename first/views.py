from rest_framework.response import Response
from rest_framework.views import APIView


# request тут
class FirstView(APIView):
    def get(self, request):
        return Response('Method Get')

    def post(self, request):
        return Response('Method Post')

    def put(self, request):
        return Response('Method Put')

    def patch(self, request):
        return Response('Method Patch')

    def delete(self, request):
        return Response('Method Delete')
