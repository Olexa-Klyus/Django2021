from rest_framework.response import Response
from rest_framework.views import APIView


# request тут обовязковий параметр
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


# для витягування  параметрів користуємося self.request, а обовязковий параметр request
# ховаємо в args, щоб не муляв очі, тому що він не типізований
class SecondView(APIView):
    def get(self, *args, **kwargs):
        query_params = self.request.query_params.dict()
        print(query_params)
        return Response(query_params)

    # передавання через body
    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response(data)


# передавання через динамічну частину урли і іменовані параметри, які попадають  в kwargs
class ThirdView(APIView):
    def get(self, *args, **kwargs):
        name = kwargs.get('name')
        age = kwargs.get('age')
        print(age)
        print(name)
        print(kwargs)
        return Response(kwargs)
