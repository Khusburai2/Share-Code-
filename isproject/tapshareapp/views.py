from django.shortcuts import render, redirect
import random
import string
from .models import SharedContent
from .forms import ContentForm

def generate_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.code = generate_code()
            content.save()
            return redirect('share_content_with_code', code=content.code)
    else:
        form = ContentForm()
    return render(request, 'tapshareapp/create_content.html', {'form': form})

def share_content(request, code=None):
    if code is None:
        code = request.GET.get('code')
    if code:
        content = SharedContent.objects.get(code=code)
        return render(request, 'tapshareapp/share_content.html', {'content': content, 'code': code})
    else:
        return redirect('create_content')
