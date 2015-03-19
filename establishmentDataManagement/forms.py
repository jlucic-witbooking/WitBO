from django import forms
from django.contrib.auth.forms import UserCreationForm
from establishmentDataManagement.utils import user_exists
from django.utils.translation import ugettext_lazy as _
from witbooking_auth.models import WitbookingUser, EstablishmentGroup


class WitbookingUserCreationForm(UserCreationForm):
    """
    Override the default UserCreationForm to force email-as-username behavior.
    """
    email = forms.EmailField(label=_("Email"), max_length=75)

    class Meta:
        model = WitbookingUser
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super(WitbookingUserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    def clean_email(self):
        email = self.cleaned_data["email"]
        if user_exists(email):
            raise forms.ValidationError(_("A user with that email already exists."))
        return email

    def save(self, commit=True):
        # Ensure that the username is set to the email address provided,
        # so the user_save_patch() will keep things in sync.
        self.instance.username = self.instance.email
        return super(WitbookingUserCreationForm, self).save(commit=commit)


class WitbookingUserChangeForm(forms.ModelForm):
    temp_id = forms.ModelMultipleChoiceField(queryset=EstablishmentGroup.objects.all())

    class Meta:
        model = WitbookingUser
        fields = '__all__'

    def is_valid(self):
        return super(WitbookingUserChangeForm, self).is_valid()
