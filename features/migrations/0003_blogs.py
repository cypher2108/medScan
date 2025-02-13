# Generated by Django 3.1.3 on 2020-11-23 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0002_auto_20201123_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heading', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=10000)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_name', to=settings.AUTH_USER_MODEL)),
                ('pat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pat_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
