# Generated by Django 1.11.21 on 2019-06-24 17:47


from django.db import migrations


def add_dynamic_conditional_offer(apps, schema_editor):
    Condition = apps.get_model('offer', 'Condition')
    new_dynamic_condition = Condition(proxy_class='ecommerce.extensions.offer.dynamic_conditional_offer.DynamicDiscountCondition')
    new_dynamic_condition.save()

    Benefit = apps.get_model('offer', 'Benefit')
    # The value doesn't matter, because it's dynamic, but oscar will complain without one.
    new_dynamic_benefit = Benefit(value=1, proxy_class='ecommerce.extensions.offer.dynamic_conditional_offer.DynamicPercentageDiscountBenefit')
    new_dynamic_benefit.save()

    ConditionalOffer = apps.get_model('offer', 'ConditionalOffer')
    new_dynamic_conditional_offer = ConditionalOffer(
        name='dynamic_conditional_offer',
        benefit=new_dynamic_benefit,
        condition=new_dynamic_condition,
        max_basket_applications=1,
        priority=-10
    )
    new_dynamic_conditional_offer.save()

def remove_dynamic_conditional_offer(apps, schema_editor):
    ConditionalOffer = apps.get_model('offer', 'ConditionalOffer')
    new_dynamic_conditional_offer = ConditionalOffer.objects.get(name='dynamic_conditional_offer')
    new_dynamic_conditional_offer.delete()

    Condition = apps.get_model('offer', 'Condition')
    new_dynamic_condition = Condition.objects.get(
        proxy_class='ecommerce.extensions.offer.dynamic_conditional_offer.DynamicDiscountCondition')
    new_dynamic_condition.delete()

    Benefit = apps.get_model('offer', 'Benefit')
    new_dynamic_benefit = Benefit.objects.get(
        proxy_class='ecommerce.extensions.offer.dynamic_conditional_offer.DynamicPercentageDiscountBenefit')
    new_dynamic_benefit.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0024_add_history_models_de_1424'),
    ]

    operations = [
        migrations.RunPython(add_dynamic_conditional_offer, remove_dynamic_conditional_offer),
    ]
