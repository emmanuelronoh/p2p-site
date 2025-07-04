# Generated by Django 5.2.3 on 2025-06-14 15:21

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('exchange_code', models.CharField(editable=False, max_length=8, unique=True)),
                ('password_hash', models.CharField(editable=False, max_length=128)),
                ('session_salt', models.CharField(editable=False, max_length=32)),
                ('client_token', models.CharField(editable=False, help_text='SHA3-256(salt + password_hash)', max_length=64, unique=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('total_trades', models.PositiveIntegerField(default=0)),
                ('success_rate', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_active', models.DateTimeField(blank=True, null=True)),
                ('trust_score', models.SmallIntegerField(default=100, help_text='0-100 reputation score', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_type', models.SmallIntegerField(choices=[(1, 'Login'), (2, 'Trade'), (3, 'Dispute'), (4, 'Admin')])),
                ('actor_token', models.CharField(blank=True, help_text='HMAC-SHA256(actor_identity)', max_length=64)),
                ('ip_hmac', models.CharField(blank=True, help_text='HMAC-SHA256(ip_address)', max_length=64)),
                ('details_enc', models.TextField(blank=True, help_text='AEAD-encrypted JSON')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'indexes': [models.Index(fields=['event_type'], name='idx_event_type'), models.Index(fields=['actor_token'], name='idx_event_actor'), models.Index(fields=['created_at'], name='idx_event_timestamp')],
            },
        ),
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_enc', models.TextField(help_text='Encrypted security question')),
                ('answer_enc', models.TextField(help_text='Encrypted answer')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_used', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='security_questions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='anonymoususer',
            index=models.Index(fields=['exchange_code'], name='idx_user_exchange_code'),
        ),
        migrations.AddIndex(
            model_name='anonymoususer',
            index=models.Index(fields=['client_token'], name='idx_user_client_token'),
        ),
    ]
