# Daily Expense Sharing: Django

A backend created for Daily Expense Sharing. Using this, user can create an expense and can split with existing user using this application. 

- User can register themselves using name, email and phone number.
- User can retrive their details
- User can add expenses.
- User can retrive individual expense detail.
- User can retrive their expenses.
- User can also retrieve their overall expenses.
- User can split expense using three methods:
  - Equal: User can split equally among all participants.
  - Exact: User can specify the exact amount each participant owes.
  - Percentage: User can specify the percentage each participant owes.

# Local setup:

Clone the repo
```
git clone git@github.com:ritikprajapat21/daily-expense-sharing-django-backend.git expense

cd expense

pip install -r requirement.txt
```
Before running, migrate the models:
```
python manage.py makemigrations
python manage.py migrate
```

To run the application:
```
python manage.py runserver
```