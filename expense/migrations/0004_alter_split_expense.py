# Generated by Django 5.0.7 on 2024-07-30 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_rename_user_expense_created_by_expense_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='split',
            name='expense',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expense.expense'),
        ),
    ]