# Generated by Django 1.11.29 on 2020-03-11 12:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0032_auto_20200305_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionaloffer',
            name='priority',
            field=models.IntegerField(db_index=True, default=0, help_text='The highest priority offers are applied first', verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='historicalconditionaloffer',
            name='priority',
            field=models.IntegerField(db_index=True, default=0, help_text='The highest priority offers are applied first', verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='rangeproductfileupload',
            name='date_uploaded',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date Uploaded'),
        ),
    ]
