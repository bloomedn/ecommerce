# Generated by Django 1.11.26 on 2019-11-15 21:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_historicalcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
