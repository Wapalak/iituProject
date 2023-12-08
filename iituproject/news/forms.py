from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'review', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={'class': 'form', 'placeholder': 'Имя Фамилия'}),
            "review": TextInput(attrs={'class': 'form', 'placeholder': 'Отзыв'}),
            "full_text": Textarea(attrs={'class': 'form', 'placeholder': 'Текст отзыва'}),
            "date": DateTimeInput(attrs={'class': 'form', 'placeholder': 'Дата'})
        }