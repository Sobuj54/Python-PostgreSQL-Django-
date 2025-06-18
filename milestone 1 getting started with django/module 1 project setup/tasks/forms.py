from django import forms
from tasks.models import Task

class TaskForm(forms.Form):
    title = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateField(widget=forms.SelectDateWidget)
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])

    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees",[])
        super().__init__(*args, **kwargs)
        self.fields["assigned_to"].choices = [(emp.id, emp.name) for emp in employees]


# the class name must contain mixin
class StyledFormMixin:
    """ applying stye to the form field """
    default_classes = "border-2 border-gray-500 w-full p-2 rounded-lg"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    "class" : self.default_classes,
                    "placeholder" : f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": self.default_classes,
                    "placeholder" : f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": "border-2 border-gray-500  p-2 rounded-lg",
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class": "border-2 border-gray-500 p-2 rounded-lg",
                })
            else:
                 field.widget.attrs.update({
                    "class": self.default_classes,
                })

# Model form
class TaskModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        # fields = "__all__" creates form for all the fields in model
        fields = ["title", "description", "due_date", "assigned_to"]
        # exclude = ["project", "is_completed", "created_at", "updated_at"] this will exclude the given fields
        widgets = {
            "due_date" : forms.SelectDateWidget,
            "assigned_to" : forms.CheckboxSelectMultiple
        }

        """ manual widget apply way """
        # widgets = {
        #     "title": forms.TextInput(attrs={
        #         "class": "border-2 border-gray-500 w-full p-2 rounded-lg",
        #         "placeholder":"Enter task title"
        #     }),
        #     "description": forms.Textarea(attrs={
        #         "class": "border-2 border-gray-500 w-full rounded-lg",
        #         "placeholder":"Enter task description"
        #     }),
        #     "due_date": forms.SelectDateWidget(attrs={
        #         "class": "border-2 border-gray-500 rounded-lg",
        #     }),
        #     "assigned_to": forms.CheckboxSelectMultiple(attrs={
        #        "class": "border-2 border-gray-500 rounded-lg flex gap-3",  
        #     })
        # }

    """ widget using mixin """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
