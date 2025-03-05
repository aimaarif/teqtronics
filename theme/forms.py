from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'company_name', 'phone', 'email', 'project_detail', 'project_file']
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "w-full mt-2 p-3 border border-gray-500", "placeholder": "Your Name"}),
            'company_name': forms.TextInput(attrs={"class": "w-full mt-2 p-3 border border-gray-500", "placeholder": "Company Name"}),
            'phone': forms.TextInput(attrs={"class": "w-full mt-2 p-3 border border-gray-500", "placeholder": "Phone Number"}),
            'email': forms.EmailInput(attrs={"class": "w-full mt-2 p-3 border border-gray-500", "placeholder": "Email"}),
            'project_detail': forms.Textarea(attrs={"class": "w-full mt-2 p-3 border border-gray-500", "rows": "4", "placeholder": "Describe your project"}),
            'project_file': forms.FileInput(attrs={"class": "w-full mt-2 p-3"}),
        }
