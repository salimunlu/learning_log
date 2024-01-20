from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Boş bir kayıt formu oluştur
        form = UserCreationForm()
    else:
        # Doldurulmuş bir kayıt formunu işle
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

