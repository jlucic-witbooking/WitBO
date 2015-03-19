from django.contrib import auth
from django.db import models
from django.contrib.auth.models import Permission, Group, _user_get_all_permissions, _user_has_perm, \
    _user_has_module_perms
from django.utils import six
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager, Permission
from django.utils.translation import ugettext_lazy as _
from accounting.models import Establishment

__author__ = 'mongoose'

@python_2_unicode_compatible
class WitbookingPermission(Permission):
    pid = models.AutoField(primary_key=True)
    establishment = models.ForeignKey('accounting.Establishment')

    def __str__(self):
        return "%s | %s | %s" % (
            six.text_type(self.establishment),
            six.text_type(self.content_type),
            six.text_type(self.name))


class Role(models.Model):
    name = models.CharField(_('role'), max_length=255)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('roles'),
        blank=True, help_text=_('The authorization role a user has. A user will '
                                'get all permissions granted to each of '
                                'his/her role.'),
    )


class RoleWithHotel(models.Model):
    role = models.ForeignKey(Role)
    user = models.ForeignKey('WitbookingUser', null=True)
    user_group = models.ForeignKey('UserGroups', null=True)
    establishment = models.ForeignKey('accounting.Establishment')


class WitbookingPermissionsMixin(models.Model):
    """
    IMPORTANT
    WHY THIS CLASS?
    We cannot subclass the mixing and override it as normal Python would
    allow, instead we copy the whole class :(

    A mixin class that adds the fields and methods necessary to support
    Django's Group and Permission model using the ModelBackend.

    """

    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.')
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True, help_text=_('The groups this user belongs to. A user will '
                                'get all permissions granted to each of '
                                'his/her group.'),
        related_name="user_set", related_query_name="user"
    )

    user_permissions = models.ManyToManyField(
        WitbookingPermission,
        verbose_name=_('user permissions'), blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_set", related_query_name="user"
    )

    roles_with_hotel = models.ManyToManyField(
        Role,
        verbose_name=_('User roles to hotels'), blank=True,
        help_text=_('Specific roles for this user for specific hotels.'),
        through='RoleWithHotel'
    )

    class Meta:
        abstract = True
        app_label = 'witbooking_auth'

    def get_group_permissions(self, obj=None):
        """
        Returns a list of permission strings that this user has through their
        groups. This method queries all available auth backends. If an object
        is passed in, only permissions matching this object are returned.
        """
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_group_permissions"):
                permissions.update(backend.get_group_permissions(self, obj))
        return permissions

    def get_all_permissions(self, obj=None):
        return _user_get_all_permissions(self, obj)

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission. This method
        queries all available auth backends, but returns immediately if any
        backend returns True. Thus, a user who has permission from a single
        auth backend is assumed to have permission in general. If an object is
        provided, permissions for this specific object are checked.
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)


class WitbookingUser(AbstractBaseUser, WitbookingPermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(default=False)
    default_db = models.CharField(blank=True, null=True, max_length=64)
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    current_establishment = None
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'auth_user'
        abstract = False
        swappable = 'AUTH_USER_MODEL'
        app_label = 'witbooking_auth'


class EstablishmentGroup(models.Model):
    name = models.CharField(_('establishment'), max_length=255)
    establishments = models.ManyToManyField('accounting.Establishment')

    def __unicode__(self):
        return u'%s' % self.name


class UserGroups(models.Model):
    name = models.CharField(_('user_groups'), max_length=255)
    witbooking_users = models.ManyToManyField(
        WitbookingUser,
        verbose_name=_('users'),
        blank=True
    )
    group_permissions = models.ManyToManyField(
        WitbookingPermission,
        verbose_name=_('Group permissions'), blank=True,
        help_text=_('Specific permissions for this group.'),
    )
    roles_with_hotel = models.ManyToManyField(
        Role,
        verbose_name=_('Group roles to hotels'), blank=True,
        help_text=_('Specific roles for this group for specific hotels.'),
        through='RoleWithHotel'
    )
