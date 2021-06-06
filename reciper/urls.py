from django.urls import path
from . import views


urlpatterns = [
    path("",views.RecipeView.as_view()),
    path("<int:pk>/",views.RecipeDetailView.as_view()),
    path("recipe/<int:pk>/<int:usr_id>/",views.AddComment.as_view(), name='add_comment'),
    path("saveRecipe/<int:pk>/<int:usr_id>/",views.SaveRecipe.as_view(), name='save_recipe'),
    path("review/<int:pk>/",views.AddReview.as_view(), name='add_review'),
    path("report/",views.Report.as_view()),
    path("showSaved/<int:pk>/",views.SavedView.as_view(),name = "saved"),
    path("showOwn/<int:pk>/",views.ShowOwn.as_view(), name = "own"),
    path('register/', views.RegisterView.as_view(), name='register'),  # ADD NEW PATTERN!
]
