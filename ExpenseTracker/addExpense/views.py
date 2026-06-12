from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense
from datetime import date

# add expense logic
@login_required
def addExpense(request):
    if request.method == "POST":

        amount = request.POST.get("amount")
        category = request.POST.get("category")
        expense_date = request.POST.get("date")
        note = request.POST.get("note")

        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            date=expense_date,
            note=note
        )

        return redirect("allExpense")
    
    #get request
    
    return render(request, 'addExpense.html', {
        'today': date.today().isoformat(),
        'full_name': request.user.get_full_name()
    })
