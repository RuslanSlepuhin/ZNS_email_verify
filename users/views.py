
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from .models import User


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Output:": serializer.data})

class AllUsersViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
