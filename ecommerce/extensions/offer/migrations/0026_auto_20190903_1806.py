# Generated by Django 1.11.23 on 2019-09-03 18:06


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0025_auto_20190624_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='journal_bundle_uuid',
        ),
        migrations.RemoveField(
            model_name='historicalcondition',
            name='journal_bundle_uuid',
        ),
    ]
