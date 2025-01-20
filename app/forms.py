from django import forms
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'desc', 'deadline']
        
        
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
            
        }
        
    # manualvalidation logic  
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 5 or len(name)> 100:
            raise forms.ValidationError('Invalid name length')
        return name
   
   
    #add request.user to user field before saving 
    def save(self, commit=True, *args, **kwargs):
        task = super().save(commit=False)
        request = kwargs.get('request')
        task.user = request.user
        if commit:
            task.save()
        return task