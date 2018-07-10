from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView

from api.services.ElasticService import ElasticService


class ResetView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        ElasticService().drop_database(
            index='*')
        return Response(status=204)


class ResetIndexView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        ElasticService().drop_database(
            index=self.kwargs['index'])
        return Response(status=204)