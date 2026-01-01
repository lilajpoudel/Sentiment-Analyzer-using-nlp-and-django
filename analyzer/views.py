from django.shortcuts import render
from .forms import SentimentForm
from .utils import predict_sentiment

def analyze_text(request):
    result = None
    if request.method == "POST":
        form = SentimentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = predict_sentiment(text)
    else:
        form = SentimentForm()
    return render(request, 'analyzer/analyze.html', {'form': form, 'result': result})
