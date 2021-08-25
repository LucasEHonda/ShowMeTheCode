from rest_framework import authentication, permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from calls.api import serializers
from calls.models import Call


class CallsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Calls
    read_only_serializer = serializers.CallsMyDetail
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        return Response(response)

    def list(self, request):
        calls = self.get_queryset()
        serialized_calls = self.read_only_serializer(instance=calls, many=True).data
        return Response(serialized_calls)

    def get_queryset(self):
        return Call.objects.filter(user=self.request.user.id)
