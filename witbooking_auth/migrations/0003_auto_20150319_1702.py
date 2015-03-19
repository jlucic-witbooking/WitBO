# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('accounting', '0003_auto_20150316_1322'),
        ('witbooking_auth', '0002_establishmentgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='role')),
                ('permissions', models.ManyToManyField(help_text='The authorization role a user has. A user will get all permissions granted to each of his/her role.', to='auth.Permission', verbose_name='roles', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoleWithHotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('establishment', models.ForeignKey(to='accounting.Establishment')),
                ('role', models.ForeignKey(to='witbooking_auth.Role')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='user_groups')),
                ('group_permissions', models.ManyToManyField(help_text='Specific permissions for this group.', to='witbooking_auth.WitbookingPermission', verbose_name='Group permissions', blank=True)),
                ('roles_with_hotel', models.ManyToManyField(help_text='Specific roles for this group for specific hotels.', to='witbooking_auth.Role', verbose_name='Group roles to hotels', through='witbooking_auth.RoleWithHotel', blank=True)),
                ('witbooking_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='users', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rolewithhotel',
            name='user_group',
            field=models.ForeignKey(to='witbooking_auth.UserGroups', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='witbookinguser',
            name='roles_with_hotel',
            field=models.ManyToManyField(help_text='Specific roles for this user for specific hotels.', to='witbooking_auth.Role', verbose_name='User roles to hotels', through='witbooking_auth.RoleWithHotel', blank=True),
            preserve_default=True,
        ),
    ]
