# Generated by Django 2.2.8 on 2020-02-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0052_answer_isdisabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='remarks',
            field=models.CharField(blank=True, default=None, max_length=3000, null=True),
        ),
    ]
