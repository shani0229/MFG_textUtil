# # Create your views here.
# from django.shortcuts import render
# from django.http import HttpResponse

# def analzer(request):
#     djtext = request.GET.get('text','default')
#     removepunc = request.GET.get('removepuch','off')
#     print(removepunc)
#     print(djtext)
#     analyzed = djtext
#     punctuation='''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
#     analyzed = ""
#     for char in djtext: 
#         if char not in punctuation:
#             analyzed = analyzed + char


#     params = {'perpose':'removed punctuations','analzer_text':'analyzed'}
#     return render(request,'analzer.html',params)

#     #return HttpResponse("removepunc")
# def home(request):
#     return render(request,'home.html')
    

# #     #return HttpResponse("<h1>Hello Word</h1>")

# # def about(request):
# #     return HttpResponse("<h1>allahabad Word</h1>")
   
# # def shani(request):
# #     return HttpResponse("<h1>Noida Word</h1>")
   


# Views.py
# I have created this file - Harry
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''For Entertainment youtube video''',
             '''For Interaction Facebook''',
             '''For Insight   Ted Talk''',
             '''For Internship   Intenship''',
             ]
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")





