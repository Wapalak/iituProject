from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'review', 'full_text']

        widgets = {
            "title": TextInput(attrs={'class': 'form', 'placeholder': 'Имя Фамилия'}),
            "review": TextInput(attrs={'class': 'form', 'placeholder': 'Краткий отзыв'}),
            "full_text": Textarea(attrs={'class': 'form', 'placeholder': 'Текст отзыва'}),
            "date": DateTimeInput(attrs={'class': 'form', 'placeholder': 'Дата'})
        }
