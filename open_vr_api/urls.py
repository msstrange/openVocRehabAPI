"""openVocRehab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from open_vr_api.views.login import login
from open_vr_api.views.individual_characteristics import IndividualCharacteristicsDetail
from open_vr_api.views.application import ApplicationDetail
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', GraphQLView.as_view(graphiql=True)),
    path('login/', login, name='login'),
    path('application/', ApplicationDetail.as_view(), name='application'),
    path('individual_characteristics/', IndividualCharacteristicsDetail.as_view(),
         name='individual_characteristics'),
]
