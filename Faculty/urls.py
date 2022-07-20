from django.urls import path,include
from . import views
app_name='faculty'
urlpatterns = [

    path('',views.Teachers.as_view(),name='teachers'),
    path('profile/<int:pk>',views.TeacherProfile.as_view(),name='profile'),
    path('delete/<int:pk>',views.RemoveTeacher.as_view(),name='remove'),
    path('profile/update/<int:pk>/',views.UpdateProfile.as_view(),name='update'),
    path('New/',views.NewTeacher.as_view(),name='newteacher'),
]