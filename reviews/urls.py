from django.urls import path
from reviews.views import *

urlpatterns = [
   
   path('home/',home,name='home'),
   path('login/',login_page,name='login_page'),
   path('register/',register,name='register'),
   path('reviews/',stu_reviews,name='stu_reviews'),
   path('logout_page/',logout_page,name='logout_page'),
   #  path("<int:update_id>/",update_feedback,name="update_feedback"),
   path("delete_feedback/<int:delete_id>/",delete_feedback,name="delete_feedback"),
   path("update_feedback/<int:update_id>/",update_feedback,name="update_feedback"),
  
  

]