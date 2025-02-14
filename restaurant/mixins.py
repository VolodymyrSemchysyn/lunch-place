from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class VersionedAPIView(APIView):
    SUPPORTED_VERSIONS = ["1.0", "2.0"]

    def dispatch(self, request, *args, **kwargs):
        build_version = request.headers.get("Build-Version")
        if build_version and build_version not in self.SUPPORTED_VERSIONS:
            return Response({"error": "Unsupported version"}, status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request, *args, **kwargs)
