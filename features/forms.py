from django.contrib.auth.forms import UserChangeForm

from user_model.models import Account


class EditPatientProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'email',
            'age',
            'gender',
            'mobile',
            'address',
        )


class EditDoctorProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'email',
            'age',
            'gender',
            'mobile',
            'address',
            'specialization',
        )
