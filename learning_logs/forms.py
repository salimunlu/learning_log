from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    # EntryForm, kullanıcıdan 'Entry' metni almak için özel olarak tasarlanmış bir formdur.
    class Meta:
        model = Entry   # Form Entry modeline dayanıyor
        fields = ['text']   # Sadece text alanı bu forma dahil edildi
        labels = {'text': ''}  # 'text' alanına boş bir etiket atandı.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # 'text' alanı için bir HTML form elemanı

