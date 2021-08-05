# Generated by Django 1.11.11 on 2018-07-10 11:29


from django.db import migrations
from oscar.apps.catalogue.categories import create_from_breadcrumbs
from oscar.core.loading import get_model

Category = get_model('catalogue', 'Category')

COUPON_CATEGORY_NAME = 'Coupons'

DEFAULT_CATEGORIES = [
    'Bulk Enrollment - Prepay',
    'Bulk Enrollment - Upon Redemption',
    'Bulk Enrollment - Integration',
]

def create_default_categories(apps, schema_editor):
    """Create default coupon categories."""
    Category.skip_history_when_saving = True

    for category in DEFAULT_CATEGORIES:
        create_from_breadcrumbs(f'{COUPON_CATEGORY_NAME} > {category}')


def remove_default_categories(apps, schema_editor):
    """Remove default coupon categories."""
    Category.skip_history_when_saving = True
    Category.objects.get(name=COUPON_CATEGORY_NAME).get_children().filter(
        name__in=DEFAULT_CATEGORIES
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('catalogue', '0032_journal_product_class'),
    ]

    operations = [
        migrations.RunPython(create_default_categories, remove_default_categories)
    ]
