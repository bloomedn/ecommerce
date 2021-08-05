from django.db import migrations

from ecommerce.enterprise.constants import ENTERPRISE_OFFERS_SWITCH


def create_switch(apps, schema_editor):
    """Create the `enable_enterprise_offers` switch if it does not already exist."""
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.update_or_create(name=ENTERPRISE_OFFERS_SWITCH, defaults={'active': False})


def delete_switch(apps, schema_editor):
    """Delete the `enable_enterprise_offers` switch."""
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.filter(name=ENTERPRISE_OFFERS_SWITCH).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_switch, delete_switch)
    ]
