from .models import User
from django import forms

#USERを作成するForm
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userid', 'email', 'password')

    # password validation 
    def clean_password(self):
        password = self.cleaned_data['password'] #まだ入れてない
        return password
    
    
    def save(self, commit=True):
        user = super().save(commit=False) # DBにまだいれない/  commit parameter controls whether the user instance is saved to the database immediately
        user.set_password(self.cleaned_data['password'])
        if commit: 
            user.save()
        return user