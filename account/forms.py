from .models import User

from django import forms

#USERを作成するForm
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userid', 'email', 'password')

    # cleaning password
    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user