
from .views import AllUsersViewsets, RegisterView
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('create/', RegisterView.as_view()),
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]