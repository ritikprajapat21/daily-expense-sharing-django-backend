from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import json
from .models import Expense, Split
from .services import equal_split, exact_split, percentage_split

User = get_user_model()

def add_user(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        name = body['name']
        phone_number = body['phone_number']
        email = body['email']
        password = body['password']

        # Checking if user exists
        user_exist = User.objects.filter(email=email)

        if user_exist.exists():
            return JsonResponse({'error': 'User with given email already exists'})

        user = User.objects.create(name=name, phone_number=phone_number, email=email)
        user.set_password(password)
        user.save()

        return JsonResponse({'message': 'User added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_user(request, id):
    user = User.objects.filter(pk=id).values('id', 'name', 'phone_number', 'email')

    if not user.exists():
        return JsonResponse({'error': 'User not found. Please add user'}, status=404)
    
    data = {'user': list(user)}

    return JsonResponse({'data':data})

def add_expense(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        user_id = body['user_id']
        total_amount = body['amount']

        try:
            user = User.objects.filter(pk=user_id).first()

            Expense.objects.create(created_by=user, total_amount=total_amount)
            
            return JsonResponse({'message': 'Expense added successfully'}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'User does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_expense(request, id):
    expense = Expense.objects.filter(pk=id)

    if not expense.exists():
        return JsonResponse({'error': 'Expense does not exist'}, status=404)
    
    split = list(expense[0].split.all().values('id', 'amount', 'user', 'split_method'))
    expense = list(expense.values('id', 'created_by', 'total_amount', 'created_at'))[0]

    return JsonResponse({'data': {'expense': expense, 'split': split}})

def get_expenses(request):
    body = json.loads(request.body.decode('utf-8'))

    user_id = body['user_id']

    try:
        user = User.objects.get(pk=user_id)

        if not user:
            raise IntegrityError('User does not exist')

        expenses = user.expenditure.all().values('id', 'total_amount', 'created_at')

        return JsonResponse({'data': {'expense': list(expenses)}})
    except IntegrityError as e:
        return JsonResponse({'error': e.message})

def get_overall_expense(request):
    body = json.loads(request.body.decode('utf-8'))

    user_id = body['user_id']
    try:
        user = User.objects.get(pk=user_id)

        if not user:
            raise IntegrityError('User not found')
        
        expenses = user.expenditure.all()
        data = []

        for expense in expenses:
            expense_id = expense.id
            split = list(expense.split.all().values('id', 'amount', 'user', 'split_method'))
            data.append({'expense': expense_id, 'split': split})
        
        return JsonResponse({'data': data})
    except IntegrityError as e:
        return JsonResponse({'error': e.message}, status=404)
    

def set_split(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))

            split_method = body['split_method']
            expense_id  = body['expense_id']
            expense = Expense.objects.filter(pk=expense_id).first()
            if not expense:
                raise IntegrityError('Expense does not exist')
            
            if len(expense.split.all()) > 0:
                return JsonResponse({'error': 'Split already created'})

            if split_method == 'EQ':
                # user_ids is a list of user ids
                user_ids = body['user_ids']
                users = User.objects.filter(id__in=user_ids)
                splits = equal_split(expense, users)
            elif split_method == 'EX':
                # user_amounts is a dictionary where key is user id and value is exact amount
                user_amounts = body['user_amounts']
                splits = exact_split(expense, user_amounts)
            elif split_method == 'PE':
                # user_percentage_amounts is a dictionary where key is user id and value is percentage
                user_percentage = body['user_percentage_amounts']
                splits = percentage_split(expense, user_percentage)
            else:
                raise ValidationError('Invalid split method')

            Split.objects.bulk_create(splits)

            return JsonResponse({'message': "Split created successfully"})
        except Exception as e:
            return JsonResponse({'error': e.message}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
