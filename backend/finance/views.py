from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import incomeForm, expenseForm
from .models import income, expense
from django.db.models import Sum
from django.contrib.auth.models import User
# Create your views here.

def stock(request):
    return render(request,'home.html')

@login_required(login_url='login')
def loginrestricted(request):
    return render(request, 'login-restricted.html')
@login_required(login_url='login')
def incomeform(request):
    user_id = request.user.id
    form=incomeForm()
    if request.method=='POST':
        form=incomeForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = request.user.id
            form.save()
    context={'form':form}
    return render(request,'income-form.html', context)
def allincome(request):
    currentU=request.user
    print(currentU)
    if request.method=='POST':
        datef=request.POST['date-from']
        datet=request.POST['date-to']
        show=income.objects.filter(In_date__gte=datef, In_date__lte=datet)
        searchincome=income.objects.filter(In_date__gte=datef, In_date__lte=datet).aggregate(Sum("In_amount"))
        return render(request,'income-list.html',{'show':show,'searchincome':searchincome,'search':search})
    else:
        incomelist=income.objects.filter(user=currentU).values()
        total_monthly_income = income.objects.aggregate(Sum('In_amount'))
        context={'incomelist':incomelist, 'total_monthly_income':total_monthly_income}
        return render(request, 'income-list.html',context)

#expense code
@login_required(login_url='login')
def expenseform(request):
    form=expenseForm()
    if request.method=='POST':
        form=expenseForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'expense-form.html', context)

def allexpense(request):
    if request.method=='POST':
        datef=request.POST['date-from']
        datet=request.POST['date-to']
        show=expense.objects.filter(Ex_date__gte=datef, Ex_date__lte=datet)
        searchincome=expense.objects.filter(Ex_date__gte=datef, Ex_date__lte=datet).aggregate(Sum("Ex_amount"))
        return render(request,'expense-list.html',{'show':show,'searchincome':searchincome,'search':search})
    else:
        incomelist=expense.objects.all()
        total_monthly_income = expense.objects.aggregate(Sum('Ex_amount'))
        context={'incomelist':incomelist, 'total_monthly_income':total_monthly_income}
        return render(request, 'expense-list.html',context)