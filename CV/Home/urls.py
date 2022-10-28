from django.urls import path
from Home import views


urlpatterns = [
    path('',views.home),
    path('show',views.show),
    path('view/<int:id>/',views.view),
    path('send',views.send),
    path('delete/<int:id>/',views.delete),
    path('edit/<int:id>',views.edit),
    path('RecordEdited',views.RecordEdited),
]
