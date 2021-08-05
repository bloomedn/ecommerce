# Generated by Django 1.10.7 on 2017-10-04 14:30

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0012_condition_program_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseAbsoluteDiscountBenefit',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.absolutediscountbenefit',),
        ),
        migrations.CreateModel(
            name='EnterprisePercentageDiscountBenefit',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.percentagediscountbenefit',),
        ),
        migrations.CreateModel(
            name='EnterpriseCustomerCondition',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.condition',),
        ),
    ]
