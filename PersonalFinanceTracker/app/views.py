# app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, Category
from .forms import IncomeForm, ExpenseForm

@login_required
def dashboard(request):
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': sum([income.amount for income in incomes]),
        'total_expense': sum([expense.amount for expense in expenses]),
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_income(request):
    form = IncomeForm()
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    return render(request, 'income_form.html', {'form': form})

@login_required
def add_expense(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    return render(request, 'expense_form.html', {'form': form})

@login_required
def delete_income(request, pk):
    income = Income.objects.get(pk=pk, user=request.user)
    if income:
        income.delete()
    return redirect('dashboard')

@login_required
def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk, user=request.user)
    if expense:
        expense.delete()
    return redirect('dashboard')
