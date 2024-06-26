# Generated by Django 4.2.5 on 2024-04-19 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_delete_fine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('paid', models.BooleanField(default=False, verbose_name='Is user paid')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unpaid_fines', to='books.book', verbose_name='Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fines', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Fine',
                'verbose_name_plural': 'Fines',
            },
        ),
    ]
