from django import forms


class AddToCartForms(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, required=False)
    weight = forms.IntegerField(initial=1, min_value=1, required=False)
