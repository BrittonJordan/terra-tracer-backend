from django.urls import path

from user.views import UserList, UserDetail, DummyUser, VisitPOI, GetPOIVisits, GetPOIVisitByIds

urlpatterns = [
    path('list', UserList.as_view(), name='user-list'),
    path('visit-poi', VisitPOI.as_view(), name='visit-poi'),
    path('get-poi-by-ids', GetPOIVisitByIds.as_view(), name='get-poi-by-ids'),
    path('get-poi-visits', GetPOIVisits.as_view(), name='get-poi-visits'),
    path('<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('dummy-users/<int:num>', DummyUser.as_view(), name='dummy-user')

]
