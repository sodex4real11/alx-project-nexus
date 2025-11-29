from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE INDEX idx_product_price_category ON products_product (price, category_id) WHERE is_active = true;"
        ),
        migrations.RunSQL(
            "CREATE INDEX idx_product_search ON products_product USING gin (to_tsvector('english', name || ' ' || description));"
        ),
        migrations.RunSQL(
            "CREATE INDEX idx_category_tree ON products_category (parent_id, is_active);"
        ),
    ]
