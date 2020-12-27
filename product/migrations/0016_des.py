# Generated by Django 3.1.1 on 2020-10-21 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20201021_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='des',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]