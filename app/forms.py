from app.models import User, Product, Category
from django import forms

#AdminでUSERを作成するForm
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
    
# Product作成の時に末端カテゴリーからの選択
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(subcategories__isnull=True)