from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():

            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
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

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Entry'i şuanki haliyle formda sergile
        form = EntryForm(instance=entry)
    else:
        # POST verisi gönderildi. Veriyi işle
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    """Delete an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    entry.delete_entry()
    return redirect('learning_logs:topic', topic_id=topic.id)

@login_required
def delete_topic(request, topic_id):
    """Delete an existing topic."""
    topic = Topic.objects.get(id=topic_id)
    topic.delete_topic()
    return redirect('learning_logs:topics')
