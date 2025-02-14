from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class VersionedAPIView(APIView):
    SUPPORTED_VERSIONS = ["1.0", "2.0"]
    DEFAULT_VERSION = "1.0"

    def dispatch(self, request, *args, **kwargs):
        build_version = request.headers.get("Build-Version", self.DEFAULT_VERSION)
        if build_version not in self.SUPPORTED_VERSIONS:
            return Response({"error": "Unsupported version"}, status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request, *args, **kwargs)
