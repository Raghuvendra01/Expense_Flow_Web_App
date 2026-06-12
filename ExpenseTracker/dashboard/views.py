from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Budget
from addExpense.models import Expense
from django.db.models import Sum
from django.contrib.auth import logout


# dashboard
@login_required
def dashboard(request):
    if request.method == "POST":

        image = request.FILES.get("image")

        if image:

            profile, _ = Profile.objects.get_or_create(
                user=request.user
            )

            profile.image = image
            profile.save()

    profile = Profile.objects.filter(
        user=request.user
    ).first()

    budget, _ = Budget.objects.get_or_create(
        user=request.user
    )

    max_expense_category = (
    Expense.objects
    .filter(user=request.user)
    .values("category")
    .annotate(total_expense=Sum("amount"))
    .order_by("-total_expense")
    .first()
    )

    context = {
        "full_name": request.user.get_full_name(),
        "profile": profile,
        "budget": budget,
        "max_expense": max_expense_category,
    }
    return render(request, 'dashboard.html', context)


@login_required
def save_budget(request):

    if request.method == "POST":

        monthly_income = request.POST.get("monthly_income")
        total_balance = request.POST.get("total_balance")

        Budget.objects.update_or_create(
            user=request.user,
            # when we have one to one relationship then
            # for create and update we use defaults and 
            # write like key and paper to assign attribut
            defaults={
                "monthly_income": monthly_income,
                "total_balance_to_spend": total_balance,
            }
        )

    return redirect("dashboard")

def logout_view(request):
    logout(request)
    return redirect("login")

