import datetime

from django import forms

from to_do_app.base.forms import BoostrapFormMixin, DateInput, DisableFieldsFormMixin
from to_do_app.task.models import Task, Project


class ProjectCreateForm(BoostrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Project
        fields = ('title', 'priority', 'color')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter project name'
            }),
            'priority': forms.Select,
            'color': forms.Select
        }


class ProjectEditForm(BoostrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Project
        fields = '__all__'


class ProjectDeleteForm(BoostrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    def save(self, commit=True):
        tasks = list(self.instance.task_set.all())
        Project.objects.filter(task__in=tasks).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Project
        fields = '__all__'


class TaskCreateForm(BoostrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Task
        fields = ('project', 'title', 'due_date')
        widgets = {
            'project': forms.Select,
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task name'
            }),
            'due_date': DateInput(attrs={
                'min': datetime.date.today()
            })
        }


class TaskEditForm(BoostrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Task
        fields = ('project', 'title', 'due_date', 'is_completed',)
        widgets = {
            'project': forms.Select,
            'title': forms.TextInput(),
            'due_date': forms.SelectDateWidget,
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class TaskDeleteForm(BoostrapFormMixin, DisableFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()
        self._init_disable_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Task
        fields = ('project', 'title', 'due_date', 'is_completed',)
        widgets = {
            'project': forms.Select,
            'title': forms.TextInput(),
            'due_date': forms.SelectDateWidget,
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
