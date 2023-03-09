from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mappin/', views.mappin_form,name='mappinform'),
    path('retrieve/',views.retrieve,name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),

    path('location/', views.location_form,name='location_form'),
    path('retrieves/',views.retrievedata,name="retrievedata"),
    path('edits/<int:id>',views.editdata,name="editdata"),
    path('updates/<int:id>',views.updatedata,name="updatedata"),
    path('deletes/<int:id>',views.deletedata,name="deletedata"),
    path('maps/', views.mapscity,name='mapscity'),
]