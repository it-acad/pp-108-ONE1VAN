from django import forms
from .models import Order
from book.models import Book

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'plated_end_at']
        widgets = {
            'plated_end_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(count__gt=0)
        self.fields['book'].label_from_instance = lambda obj: obj.name