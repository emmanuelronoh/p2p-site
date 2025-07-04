# Generated by Django 5.2.1 on 2025-06-23 09:24

import apps.escrow.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escrow', '0002_escrowwallet_amount_escrowwallet_buyer_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escrowwallet',
            name='buyer_address',
            field=models.CharField(blank=True, help_text='ETH address of the buyer', max_length=42, null=True, validators=[apps.escrow.validators.validate_eth_address]),
        ),
        migrations.AlterField(
            model_name='escrowwallet',
            name='seller_address',
            field=models.CharField(blank=True, help_text='ETH address of the seller', max_length=42, null=True, validators=[apps.escrow.validators.validate_eth_address]),
        ),
        migrations.CreateModel(
            name='EscrowAuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('CREATE', 'Create'), ('FUND', 'Fund'), ('RELEASE', 'Release'), ('DISPUTE', 'Dispute')], max_length=10)),
                ('details', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('escrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_logs', to='escrow.escrowwallet')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TransactionQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx_hash', models.CharField(max_length=66)),
                ('tx_type', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Processing'), (3, 'Completed'), (4, 'Failed')], default=1)),
                ('retry_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('processed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['status'], name='idx_txqueue_status'), models.Index(fields=['tx_hash'], name='idx_txqueue_hash')],
            },
        ),
        migrations.CreateModel(
            name='EscrowDispute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiator', models.CharField(max_length=64)),
                ('reason', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'In Review'), (3, 'Resolved')], default=1)),
                ('resolution', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('escrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disputes', to='escrow.escrowwallet')),
            ],
            options={
                'indexes': [models.Index(fields=['status'], name='idx_dispute_status')],
            },
        ),
    ]
