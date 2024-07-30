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

# Sample Screenshots
Add user demo:
![User add sample](https://github.com/user-attachments/assets/55bf18ef-eb65-409b-a44f-178d57807efe)
Get user details demo:
![Get user details](https://github.com/user-attachments/assets/ab94d3ab-cbca-4828-ab49-5816b37b0e72)
Create expense demo:
![Create user expense](https://github.com/user-attachments/assets/2c884c46-1220-417a-87b5-138d74069d55)
Get all created expenses demo:
![Get all the created expenses](https://github.com/user-attachments/assets/3e348bce-31aa-440d-8216-5c6ac3671533)
Get details of an expense by id demo:
![Get details of an expense by id](https://github.com/user-attachments/assets/79fffa95-f612-4b99-96c9-177a960f31cb)
Create a split demo:
![image](https://github.com/user-attachments/assets/ef3efe1c-cf98-4cc9-bff7-cc5115642361)
Get overall expense details:
![image](https://github.com/user-attachments/assets/20015918-744e-498a-8ca8-9eea35370aed)
