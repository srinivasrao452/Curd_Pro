from django import forms

class InsertingDataForm(forms.Form):
    product_number = forms.IntegerField(
        label= "Enter Product Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Number'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter Product Class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    product_weight = forms.IntegerField(
        label="Enter Product Weight",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Weight'
            }
        )
    )

class UpdatingDataForm(forms.Form):
    product_number = forms.IntegerField(
        label="Enter Product Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Number'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product New Cost'
            }
        )
    )


class DeletingDataForm(forms.Form):
    product_number = forms.IntegerField(
        label="Enter Product Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Number'
            }
        )
    )

