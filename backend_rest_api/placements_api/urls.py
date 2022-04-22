from django.urls import path
# from rest_framework.decorators import permission_classes, authentication_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import views

urlpatterns = [
    
    # PLACEMENTS
    path('api/placements', views.PlacementList.as_view(), name='placement_list'), # api/placements will be routed to the PlacementList view for handling
    path('api/placements/<int:pk>', views.PlacementDetail.as_view(), name='placement_detail'), # api/placements will be routed to the PlacementDetail view for handling
    
    # PARENTS
    path('api/parents', views.ParentList.as_view(), name='parent_list'),
    path('api/parents/<int:pk>', views.ParentDetail.as_view(), name='parent_detail'),

    #SIBLINGS
    path('api/siblings', views.SiblingList.as_view(), name='sibling_list'),
    path('api/siblings/<int:pk>', views.SiblingDetail.as_view(), name='sibling_detail'),
]

# path('', authentication_classes([])(permission_classes([AllowAny])(some_view)).as_view())