from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from addExpense.models import Expense
from dashboard.models import Profile


@login_required
def allExpense(request):

    # Current logged-in user ke saare expenses lao
    expenses = Expense.objects.filter(
        user=request.user
    )

    # URL se category value lo
    # Example:
    # /allExpense/?category=food
    # selected_category = "food"
    selected_category = request.GET.get("category")

    # Agar user ne koi category select ki hai
    # to us category ke expenses hi rakho
    if selected_category:
        expenses = expenses.filter(
            category=selected_category
        )

    # Latest expense sabse upar dikhane ke liye
    expenses = expenses.order_by("-date")

    # User ke expenses me jitni unique categories hain
    # unki list nikalo dropdown ke liye
    #
    # Example:
    # food
    # shopping
    # food
    # transport
    #
    # Result:
    # ["food", "shopping", "transport"]
    categories = Expense.objects.filter(
        user=request.user
    ).values_list(
        "category",
        flat=True
    ).distinct()

    # Current user ki profile photo/details lao
    profile = Profile.objects.filter(
        user=request.user
    ).first()

    # Template ko data bhejo
    return render(
        request,
        "allExpense.html",
        {
            # Filtered ya unfiltered expenses
            "expenses": expenses,

            # User ka full name
            "full_name": request.user.get_full_name(),

            # Profile object
            "profile": profile,

            # Abhi selected category
            # Example: food
            "selected_category": selected_category,

            # Dropdown me dikhane wali categories
            "categories": categories,
        }
    )

def delete_expense(request, id):
    expense= get_object_or_404(Expense, id=id)
    if request.method == "POST":
        expense.delete()

    return redirect("allExpense")