from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username
    


class Budget(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="budget"
    )

    monthly_income = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_balance_to_spend = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Budget"