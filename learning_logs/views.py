from django.shortcuts import render, redirect

from .forms import TopicForm, EntryForm
from .models import Topic


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry."""
    topic = Topic.objects.get(id=topic_id)   # URL'den gelen topic_id'yi kullanarak ilgili konu alınır
    # HTTP isteği türüne (GET, POST) göre işlem yapıyoruz.
    if request.method != 'POST':
        # Veri gönderilmediyse boş form oluştur
        form = EntryForm()
    else:
        # POST verisi gönderildiyse, veriyi işle.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Form geçerli ise veritabanına kaydetmeden önce entry nesnesinin topic özelliğini ayarla
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
