# Generated by Django 1.10.7 on 2017-11-07 15:50


from django.conf import settings
from django.db import migrations

from ecommerce.extensions.payment.processors.stripe import Stripe


def create_switch(apps, schema_editor):
    Switch = apps.get_model('waffle', 'Switch')
    Switch(name=settings.PAYMENT_PROCESSOR_SWITCH_PREFIX + Stripe.NAME, active=True).save()


def delete_switch(apps, schema_editor):
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.get(name=settings.PAYMENT_PROCESSOR_SWITCH_PREFIX + Stripe.NAME).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('payment', '0017_auto_20170328_1445'),
    ]

    operations = [
        migrations.RunPython(create_switch, delete_switch)
    ]
