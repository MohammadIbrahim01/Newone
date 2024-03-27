from django.shortcuts import redirect

def auth(view_function):
    def wrapped_view(request, *args, **kwargs):
        # Check if user is authenticated
        if request.user.is_authenticated == False:
            
             return redirect('hai') 
            # If authenticated, proceed with the view function
        return view_function(request, *args, **kwargs)
       
            # If not authenticated, redirect to login page
            # Adjust 'login' to your login URL name if needed
    return wrapped_view


def guest(view_function):
    def wrapped_view(request, *args, **kwargs):
        # Check if user is authenticated
        if request.user.is_authenticated:
            
             return redirect('dash')  
            # If authenticated, proceed with the view function
        return view_function(request, *args, **kwargs)
     
            # If not authenticated, redirect to login page
           # Adjust 'login' to your login URL name if needed
    return wrapped_view


