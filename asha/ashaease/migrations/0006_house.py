# Generated by Django 5.0.2 on 2024-05-12 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashaease', '0005_alter_report_created_by_heading_questions_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=20)),
                ('house_address', models.TextField()),
                ('no_of_members', models.IntegerField()),
                ('added_no_of_members', models.IntegerField()),
                ('is_no_of_members_added', models.BooleanField(default=False)),
                ('child_onboard', models.BooleanField(default=False)),
                ('child_cound', models.IntegerField()),
                ('added_child_cound', models.IntegerField()),
                ('is_child_added', models.BooleanField(default=False)),
                ('pregnant_onboard', models.BooleanField(default=False)),
                ('pregnant_cound', models.IntegerField()),
                ('added_pregnant_cound', models.IntegerField()),
                ('is_pregnant_added', models.BooleanField(default=False)),
                ('patients_onboard', models.BooleanField(default=False)),
                ('patients_cound', models.IntegerField()),
                ('added_patients_cound', models.IntegerField()),
                ('is_patients_added', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
