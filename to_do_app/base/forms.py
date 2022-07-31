from django import forms

from to_do_app.base.models import Profile
from to_do_app.task.models import Task, Project


class BoostrapFormMixin:
    fields = {}

    def _init_bootstrap_form_control(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class DisableFieldsFormMixin:
    fields = {}
    disabled_field = '__all__'

    def _init_disable_fields(self):
        for name, field in self.fields.items():
            if self.disabled_field != '__all__' and name not in self.disabled_field:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'


class ProfileCreteForm(BoostrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email'
            }),
        }


class DateInput(forms.DateInput):
    input_type = 'date'
    format_key = '%d/%m/%Y'


class ProfileEditForm(BoostrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()
        if self.initial['gender'] is None:
            self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'picture', 'day_of_birth', 'gender')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email'
            }),
            'day_of_birth': DateInput(attrs={
                'min': '1920-01-01'
            })
        }


class ProfileDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        tasks = list(self.instance.task_set.all())
        Project.objects.filter(priority__project__task__in=tasks).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
