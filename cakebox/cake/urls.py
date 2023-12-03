from django.urls import path

from cake.views import SignUpView,SignInView,CategoryCreateView,remove_category,CakeCreateView,CakeListView,CakeUpdateView\
,remove_cakeview,CakeVarientCreateView,CakeDetailView,CakeVarientUpdateView,remove_varient,OfferCreateView,remove_offer\
,sign_out_view



urlpatterns=[

    path("register/",SignUpView.as_view(),name="signup"),
    path("categories/add",CategoryCreateView.as_view(),name="category-add"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cake/add",CakeCreateView.as_view(),name="cake-add"),
    path("cake/all",CakeListView.as_view(),name="cake-list"),
    path("cake/<int:pk>/change",CakeUpdateView.as_view(),name="cake-change"),
    path("cake/<int:pk>/remove",remove_cakeview,name="cake-remove"),
    path("cake/<int:pk>/varients/add",CakeVarientCreateView.as_view(),name="add-varient"),
    path("cake/<int:pk>/",CakeDetailView.as_view(),name="cake-detail"),
    path("varients/<int:pk>/change/",CakeVarientUpdateView.as_view(),name="update-varient"),
    path("varients/<int:pk>/remove",remove_varient,name="remove-varient"),
    path("varients/<int:pk>/offers/add",OfferCreateView.as_view(),name="offers-add"),
    path("offers/<int:pk>/remove",remove_offer,name="delete-offer"),
    path("logout/",sign_out_view,name="signout"),


    
]