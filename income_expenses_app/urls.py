from django.urls import path, include
from.import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, IncomeViewSet, ExpensesViewSet
from rest_framework.authtoken import views as auth_views

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'incomes',IncomeViewSet)
router.register(r'expenses',ExpensesViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/', auth_views.obtain_auth_token)
]