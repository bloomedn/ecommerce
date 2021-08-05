# Generated by Django 1.9.13 on 2017-05-08 21:46


from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0012_condition_program_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsoluteDiscountBenefitWithoutRange',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.absolutediscountbenefit',),
        ),
        migrations.CreateModel(
            name='PercentageDiscountBenefitWithoutRange',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.percentagediscountbenefit',),
        ),
        migrations.CreateModel(
            name='ProgramCourseRunSeatsCondition',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.condition',),
        ),
    ]
