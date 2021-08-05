# Generated by Django 1.11.26 on 2019-11-15 21:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refund', '0006_historicalrefund_historicalrefundline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrefund',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Denied', 'Denied'), ('Payment Refund Error', 'Payment Refund Error'), ('Payment Refunded', 'Payment Refunded'), ('Revocation Error', 'Revocation Error'), ('Complete', 'Complete')], max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='historicalrefundline',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Revocation Error', 'Revocation Error'), ('Denied', 'Denied'), ('Complete', 'Complete')], max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Denied', 'Denied'), ('Payment Refund Error', 'Payment Refund Error'), ('Payment Refunded', 'Payment Refunded'), ('Revocation Error', 'Revocation Error'), ('Complete', 'Complete')], max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='refundline',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Revocation Error', 'Revocation Error'), ('Denied', 'Denied'), ('Complete', 'Complete')], max_length=255, verbose_name='Status'),
        ),
    ]
