import json

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.services.MongoService import MongoService
from api.services.RedisService import RedisService
from api.models.property_data import GeneratePropertyDataModel, PropertyDataModel

from sukasa.config import MONGO_DB_INFO
from analytics.property_valuation_estimator import create_property_estimation_model


SEARCH_Q = openapi.Parameter(
    name='q',
    in_=openapi.IN_QUERY,
    description='A string of search keywords',
    type=openapi.TYPE_STRING,
    required=True)

def generate_brief(property_data):
    return "{} bed {} for sale".format(
        property_data['details']['bedrooms'],
        property_data['details']['aggregateStyle']
    )

def generate_tags(property_data):
    return [
        property_data['address'].lower(),
        property_data['postcode'].lower(),
        property_data['town'].lower(),
        property_data['details']['longPostcode'].lower()
    ]

class PropertyDataView(ListCreateAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = PropertyDataModel

    @swagger_auto_schema(manual_parameters=[SEARCH_Q])
    def get(self, request, *args, **kwargs):
        search_query = self.request.GET.get('q', None)
        page = self.request.GET.get('page', 1)
        if search_query is None:
            raise ValueError(
                'Please provide some search query with the `q` query parameter')
        properties = MongoService().search_collection(
            collection_name=MONGO_DB_INFO['propertyCollection'],
            search_string=search_query.lower())
        paginator = Paginator(properties, 10)
        try:
            paginated_properties = paginator.page(page)
        except PageNotAnInteger:
            paginated_properties = paginator.page(1)
        except EmptyPage:
            paginated_properties = paginator.page(paginator.num_pages)
        return Response(
            data={
                'propertiesLength': len(properties),
                'data': paginated_properties.object_list
            },
            status=200)

    @swagger_auto_schema(responses={201: "Created"})
    def post(self, request, *args, **kwargs):
        PropertyDataModel(
            data=request.data).is_valid(
            raise_exception=True)
        request.data['brief'] = generate_brief(
            property_data=request.data)
        request.data['tags'] = generate_tags(
            property_data=request.data)
        if RedisService().check_token(
            redis_key=request.META.get('HTTP_TOKEN')):
            user_info = json.loads(RedisService().getter(
                redis_key=request.META.get('HTTP_TOKEN')))
            request.data['owner'] = user_info['_id']
        else:
            return Response(status=500)
        MongoService().insert_to_collection(
            collection_name=MONGO_DB_INFO['masterCollection'],
            data=request.data)
        return Response(status=201)


class PropertyDataIdView(RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = PropertyDataModel

    def get(self, request, *args, **kwargs):
        property = MongoService().get_from_collection(
            collection_name=MONGO_DB_INFO['propertyCollection'],
            property_id=self.kwargs['propertyId'])
        return Response(
            data=property,
            status=200)

    # TODO: Add delete property by ID
    def delete(self, request, *args, **kwargs):
        return Response(status=204)
