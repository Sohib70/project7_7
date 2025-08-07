from django.urls import path
# from .views import sumka_list,sumka_post,sumka_detail,sumka_update_put,sumka_update_patch,sumka_delete
# from .views import ListCreateApiView,DetailUpdateDelete
# from .views import ListCreateGenApiView,DetailUpdateDeleteGenApiView
from .views import ListCreateMixins,DetailUpdateDeleteMixins
urlpatterns = [

    path("",ListCreateMixins.as_view()),
    path("u/<int:pk>/",DetailUpdateDeleteMixins.as_view())
#<-------------------------------------------------------->
    # path("",ListCreateGenApiView.as_view()),
    # path("u/<int:pk>/",DetailUpdateDeleteGenApiView.as_view())
#<-------------------------------------------------------->
    # path("",ListCreateApiView.as_view()),
    # path("u/<int:pk>/",DetailUpdateDelete.as_view())
#<-------------------------------------------------------->
    # path("",sumka_list),
    # path("create/",sumka_post),
    # path("detail/<int:pk>/",sumka_detail),
    # path("put/<int:pk>/",sumka_update_put),
    # path("patch/<int:pk>/",sumka_update_patch),
    # path("delete/<int:pk>/", sumka_delete),
#<-------------------------------------------------------->

]