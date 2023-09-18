from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('creation_date', 'last_change_date')

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')

        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        for word in prohibited_words:
            if word in cleaned_name.lower():
                raise forms.ValidationError('Запрещеночка в имени товара')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')

        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        for word in prohibited_words:
            if word in cleaned_description.lower():
                raise forms.ValidationError('Запрещеночка в описании товара')

        return cleaned_description
