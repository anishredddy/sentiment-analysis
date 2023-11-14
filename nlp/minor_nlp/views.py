
from django.shortcuts import render
from .forms import FileUploadForm
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return text+"    :- Positive"
    elif sentiment_score < 0:
        return text+"    :- Negative"
    else:
        return text+"    :- Neutral"

def analyze_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_content = uploaded_file.read().decode('utf-8')

            # Perform sentiment analysis
            data=file_content.split('\n')
            res=[]
            for line in data:
                if line!="":
                    res.append(analyze_sentiment(line))
            
            return render(request, 'result.html', {'res': res})
    else:
        form = FileUploadForm()

    return render(request, 'index.html', {'form': form})

# Create your views here.
def home(request):
    return render(request,'index.html')