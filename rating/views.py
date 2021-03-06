from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status, authentication, permissions
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import RatingSerializer
from . models import Rating

from rest_framework.views import APIView

from product.models import Product
from rating.models import Rating
from .serializers import RatingSerializer
from django.db.models import Min, Max, Avg, F
from django.shortcuts import get_object_or_404
from django.http import Http404

# @api_view(['GET'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])


class AllRatingsList(APIView):
    
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        ratings = Rating.objects.filter( product=product.id )
        serializer = RatingSerializer(ratings, many=True )

        return Response(serializer.data) # todo add status 200

# class RatingsViewSet(APIView):

#     def get(self, request):
#         rating_avg =  Rating.objects.values('product__id').annotate(Max('rate'))
#         product = get_object_or_404(
#                 Product.objects.annotate(avg_score=Avg('rating__rate')),
#                 pk=1
#             )
#         return Response(rating_avg, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def rate_product(request, category_slug, product_slug):

    request.data['user'] = request.user.id
    serializer = RatingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        ratings = Rating.objects.filter(product=request.data['product'])
        Product.objects.filter(id=request.data['product']).update(counter_rating=ratings.count())
        #use this when more products/ratings
        # Product.objects.filter(id=request.data['product']).update(counter_rating=F('counter_rating') + 1)
        average_rating = Rating.objects.filter( product=request.data['product'] ).aggregate(Avg('rate'))
        Product.objects.filter(id=request.data['product']).update(average_rating=average_rating['rate__avg'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)