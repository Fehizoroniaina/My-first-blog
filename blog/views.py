from django.shortcuts import render , redirect

from mysite.forms import Post
def upload_image(request) : 
    form = Post(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('success')
    else:  
        form = Post()
    return render(request, 'upload_image.html', {'form' : form})
    
    

# Create your views here.
