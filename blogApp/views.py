from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *


class MaqolalarModleViewSet(ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerialzier


class MaqolalarAPI(APIView):
    # authentication_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        maqolalar = Maqola.objects.all().order_by("-sana")
        serializer = MaqolaSerialzier(maqolalar, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        maqola = request.data
        serializer = MaqolaSerialzier(data=maqola)
        if serializer.is_valid():
            serializer.save(muallif=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_406_NOT_ACCEPTABLE)


class MaqolaAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        maqola = Maqola.objects.get(id=pk)
        maqola.korish_soni += 1
        maqola.save()
        serializer = MaqolaSerialzier(maqola)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        maqola = Maqola.objects.get(id=pk)
        serializer = MaqolaSerialzier(maqola, data=request.data)
        if serializer.is_valid():
            serializer.save(muallif=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        maqola = Maqola.objects.get(id=pk, muallif=request.user)
        serializer = MaqolaSerialzier(maqola)
        maqola.delete()
        return Response(serializer.data)
