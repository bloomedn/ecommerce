# Generated by Django 1.11.11 on 2018-06-28 20:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20180510_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='journals_api_url',
            field=models.URLField(blank=True, null=True, verbose_name='Journals Service API URL'),
        ),
    ]
