from django import forms


class DetailsAddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'detail-quantity-input'}),
                                  initial=1)
    weight = forms.DecimalField(min_value=1,
                                widget=forms.NumberInput(attrs={'class': 'detail-quantity-input'}),
                                initial=1)


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)