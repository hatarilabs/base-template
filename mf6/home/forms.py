from django import forms
from django.forms import ModelForm
from .models import Project, SuscriptionRecords
from django.contrib.auth import get_user_model


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

class ProjectForm(ModelForm):

    class Meta:
        model = Project

        fields = ['modelName','modelDescription','timeUnitName','lengthUnitName','epsgCode','startDate']
        widgets = {'starting_date':DateTimeInput(),'ending_date':DateTimeInput(),}

        widgets = {'startDate':DateTimeInput(),}

    def __init__(self,filtered = None, *args,**kwargs):
        #filtered is the user
        if filtered is not None:
            self.filtered = filtered
        super().__init__(*args,**kwargs)
        self.fields['modelName'].widget.attrs.update({'class':'form-control','required':'required'})
        self.fields['modelDescription'].widget.attrs.update({'class':'form-control','required':'required','style': 'height:80px;'})
        self.fields['timeUnitName'].widget.attrs.update({'class':'form-control','required':'required'})
        self.fields['lengthUnitName'].widget.attrs.update({'class':'form-control','required':'required'})
        self.fields['epsgCode'].widget.attrs.update({'class':'form-control','required':'required'})
        self.fields['startDate'].widget.attrs.update({'class':'form-control','required':'required'})

    def clean(self):
        cleaned_data = super().clean()

        suscription = SuscriptionRecords.objects.filter(user = self.filtered).order_by('id').latest('id')
        projects = Project.objects.filter(user = self.filtered)
        if len(projects) >= suscription.category.n_projects:
            raise forms.ValidationError('You cannot create more projects until you update your suscription')
