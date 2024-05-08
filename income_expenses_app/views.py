from django.shortcuts import render
from rest_framework import viewsets
from .models import Income, Expenses
from .serializers import IncomeSerializer, ExpensesSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your views here.
def homepage(request):
    return render(request,'income_expenses_app/index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset= Income.objects.all()
    serializer_class=IncomeSerializer

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


class ExpensesViewSet(viewsets.ModelViewSet):
    queryset= Expenses.objects.all()
    serializer_class=ExpensesSerializer

    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)
