from .models import Split
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import get_user_model

User = get_user_model()

def equal_split(expense, users):
    """To split expense equally"""
    amount_per_user = expense.total_amount / len(users)
    splits = []
    for user in users:
        if not user:
            raise IntegrityError("User not found")
        splits.append(Split(expense=expense, user=user, amount=amount_per_user, split_method='EQ'))
    return splits

def exact_split(expense, user_amounts):
    """To split expense in exact amount"""
    total = sum(user_amounts.values())
    if total != expense.total_amount:
        raise ValidationError("The total of expense amount must be equal to total expense amount")
    splits = []
    for user_id, amount in user_amounts.items():
        user = User.objects.filter(pk=user_id).first()
        if not user:
            raise IntegrityError("User not found")
        splits.append(Split(expense=expense, user=user, amount=amount, split_method="EX"))
    return splits

def percentage_split(expense, user_percentage):
    """To split expense according to percentage"""
    total = sum(user_percentage.values())

    if total != 100:
        raise ValidationError("The total percentage must be 100%")
    
    splits = []
    total_amount = expense.total_amount
    for user_id, percentage in user_percentage.items():
        amount = (total_amount * percentage)/100
        user = User.objects.filter(pk=user_id).first()

        if not user:
            raise IntegrityError("User not found")
        splits.append(Split(expense=expense, user=user, amount=amount, split_method="PE"))

    return splits