from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template.response import TemplateResponse
from django.utils.text import capfirst
from django.views.decorators.cache import never_cache
from django.apps import apps
from django.utils import six
from establishmentDataManagement.forms import DemoUserAdminForm, WitbookingUserCreationForm
from establishmentDataManagement.models import Users
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from witbooking_auth.models import WitbookingUser, WitbookingPermission

class MyAdminSite(AdminSite):
    @never_cache
    # @permission_required('establishmentDataManagement.can_vote')
    def index(self, request, extra_context=None):
        """
        Displays the main admin index page, which lists all of the installed
        apps that have been registered in this site.
        """
        app_dict = {}
        user = request.user
        for model, model_admin in self._registry.items():
            app_label = model._meta.app_label
            has_module_perms = user.has_module_perms(app_label)

            if has_module_perms:
                perms = model_admin.get_model_perms(request)

                # Check whether user has any perm for this module.
                # If so, add the module to the model_list.
                if True in perms.values():
                    info = (app_label, model._meta.model_name)
                    model_dict = {
                        'name': capfirst(model._meta.verbose_name_plural),
                        'object_name': model._meta.object_name,
                        'perms': perms,
                    }
                    if perms.get('change', False):
                        try:
                            model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=self.name)
                        except NoReverseMatch:
                            pass
                    if perms.get('add', False):
                        try:
                            model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=self.name)
                        except NoReverseMatch:
                            pass
                    if app_label in app_dict:
                        app_dict[app_label]['models'].append(model_dict)
                    else:
                        app_dict[app_label] = {
                            'name': apps.get_app_config(app_label).verbose_name,
                            'app_label': app_label,
                            'app_url': reverse('admin:app_list', kwargs={'app_label': app_label}, current_app=self.name),
                            'has_module_perms': has_module_perms,
                            'models': [model_dict],
                        }

        # Sort the apps alphabetically.
        app_list = list(six.itervalues(app_dict))
        app_list.sort(key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        context = dict(
            self.each_context(),
            title=self.index_title,
            app_list=app_list,
        )
        context.update(extra_context or {})
        return TemplateResponse(request, self.index_template or
                                'admin/index.html', context,
                                current_app=self.name)


admin_site = MyAdminSite(name='myadmin')


class WitbookingUserAdmin(UserAdmin):
    """The project uses a custom User model, so it uses a custom User admin model.

    Some related notes at:
    https://github.com/dabapps/django-email-as-username/blob/master/emailusernames/admin.py

    And:
    .../lib/python2.7/site-packages/django/contrib/auth/admin.py
    """

    #readonly_fields = ('private_uuid', 'public_id')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'default_db')}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (
            None, {

                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    list_display = ('email', 'is_admin')
    search_fields = ('first_name', 'last_name', 'display_name', 'email')
    ordering = ('email',)
    list_filter = ('is_admin', 'is_superuser', 'is_active', 'groups')
    form = DemoUserAdminForm
    add_form = WitbookingUserCreationForm


class UsersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Users, UsersAdmin)

admin.site.register(WitbookingUser, WitbookingUserAdmin)

admin.site.register(WitbookingPermission)

admin_site.register(Users, UsersAdmin)