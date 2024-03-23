# Generated by Django 4.2.5 on 2023-11-20 07:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('AuthorId', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN10', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookLoans',
            fields=[
                ('LoanId', models.AutoField(primary_key=True, serialize=False)),
                ('Date_out', models.DateField(verbose_name=django.utils.timezone.now)),
                ('Due_Date', models.DateField(default=datetime.datetime(2023, 12, 4, 7, 42, 24, 422189, tzinfo=datetime.timezone.utc))),
                ('Date_in', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('CardId', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('SSN', models.CharField(max_length=12, unique=True)),
                ('Bname', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=2)),
                ('Phone', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fine_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Paid', models.BooleanField(default=False)),
                ('LoanId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoanId_Fines', to='LibraryManagementSystem.bookloans')),
            ],
        ),
        migrations.AddField(
            model_name='bookloans',
            name='CardId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CardId_BookLoans', to='LibraryManagementSystem.borrower'),
        ),
        migrations.AddField(
            model_name='bookloans',
            name='ISBN10',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ISBN10_BookLoans', to='LibraryManagementSystem.book'),
        ),
        migrations.CreateModel(
            name='BookAuthors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuthorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Auth', to='LibraryManagementSystem.authors')),
                ('ISBN10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ISBN10_authors', to='LibraryManagementSystem.book')),
            ],
        ),
    ]
