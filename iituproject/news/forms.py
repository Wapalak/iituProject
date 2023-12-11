from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'review', 'rating', 'full_text',]

        widgets = {
            # Виджеты для полей формы
            "title": TextInput(attrs={'class': 'form', 'placeholder': 'Имя Фамилия'}),
            "review": TextInput(attrs={'class': 'form', 'placeholder': 'Краткий отзыв'}),
            "rating": Textarea(attrs={'class': 'form', 'placeholder': 'Рейтинг'}),
            "full_text": Textarea(attrs={'class': 'form', 'placeholder': 'Текст отзыва'}),
            "date": DateTimeInput(attrs={'class': 'form', 'placeholder': 'Дата'})
        }
