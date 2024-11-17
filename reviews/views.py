from django.shortcuts import render,redirect,get_object_or_404
from reviews.models import User,feedback
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/reviews/login/')
def home(request):
    if request.method== 'POST':
        data=request.POST
        roll_no=data.get("rollno")
        student_name=data.get("studentname")
        student_reviews=data.get("review")
        if request.user.is_authenticated:
            print(roll_no,student_reviews,student_name)
            if feedback.objects.filter(roll_no=roll_no):
                messages.warning(request, "You already added your feedback thankyou.")
                return redirect('/reviews/home/')
            else:
                 feedback.objects.create(roll_no=roll_no,student_name=student_name,student_reviews=student_reviews)
                 messages.warning(request, "Your feedback is succesfully added.")
                 return redirect('/reviews/home/')
            
        else:
             messages.warning(request, "Do login first.")
             return redirect('/reviews/home/')
  
    return render(request,'index.html')

# revies page
@login_required(login_url='/reviews/login/')
def stu_reviews(request):
    queryset=feedback.objects.all()
    context={'values':queryset}     
    return render (request,'reviews.html',context)

# registration form
def register(request):
    if  request.method =='POST':
        data=request.POST
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        username=data.get('username')
        password=data.get('password')
        print(first_name,last_name,username,password)
        if User.objects.filter(username=username).exists():
             messages.warning(request, "Username already taken.")
             return redirect('/reviews/register/')
        else:


           user=User.objects.create(first_name=first_name,last_name=last_name,username=username)
           user.set_password(password)
           user.save()
           return redirect ('/reviews/login/')
    return render(request,'register.html')

# login page

def login_page(request):
    if request.method=='POST':
        data=request.POST
        username=data.get("username")
        password=data.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:     
          login(request,user)  
          return redirect('/reviews/home/')
        
        else:
            messages.warning(request, "Incorrect username or password.")
            return redirect('/reviews/login/')
    return render(request, 'login.html')

# logout 
def logout_page(request):
    logout(request)
    return redirect('/reviews/home/')

# upddate function
@login_required(login_url='/reviews/login/')
def update_feedback(request,update_id):
    user=get_object_or_404(feedback,pk=update_id)
    context={"value":user}

    if request.method == 'POST':
        data=request.POST
        roll_no=data.get("rollno")
        student_name=data.get("studentname")
        student_reviews=data.get("review")
        user.roll_no=roll_no
        user.student_name=student_name
        user.student_reviews=student_reviews
        user.save()
        return redirect('/reviews/reviews/')

    
    return render(request,'update.html',context)



# delete function 
@login_required(login_url='/reviews/login/')
def delete_feedback(request,delete_id):
    get_object_or_404(feedback,pk=delete_id).delete()

    return redirect('/reviews/reviews/')
    


 
