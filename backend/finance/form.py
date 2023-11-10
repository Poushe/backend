from django.forms import ModelForm
from finance.models import income, expense

class incomeForm(ModelForm):
    class Meta:
        model=income
        fields=['name','In_amount']

class expenseForm(ModelForm):
    class Meta:
        model=expense
        fields=['name','Ex_amount']