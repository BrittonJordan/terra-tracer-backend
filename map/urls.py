from django.urls import path

from .views import LocationList, AddLocation, DummyLocation, DummyLocationUser

urlpatterns = [
    path('get-locations/<int:uid>/', LocationList.as_view()),
    path('dummy-locations/<int:uid>/<int:num>/', DummyLocationUser.as_view()),
    path('dummy-locations/<int:num>/', DummyLocation.as_view()),

    path('add-location/', AddLocation.as_view())
]