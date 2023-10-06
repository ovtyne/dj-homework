from django import forms

from hw.models import Product, Category, Version

FORBIDDEN_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price')

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')

        for item in FORBIDDEN_WORDS:
            if item in cleaned_data.lower():
                raise forms.ValidationError('Нельзя использовать продукты из списка запрещенных')
                break

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for item in FORBIDDEN_WORDS:
            if item in cleaned_data.lower():
                raise forms.ValidationError('Нельзя использовать продукты из списка запрещенных')
                break

        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
