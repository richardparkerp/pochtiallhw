from django.urls import path
from .views import *
#7.03 
#11.03
#12.03
#14.03
#18.03
#19.03


urlpatterns = [
    path('', TODOListView.as_view(), name='index'),
    path('create/', TODOCreate.as_view(), name='create'),
    path('signup/', CreateUser.as_view(), name='signup'),
    path('update/<int:pk>/', TODOUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TODODelete.as_view(), name='delete'),
    path('detail/<int:pk>/', TODODetail.as_view(), name='detail'),
]