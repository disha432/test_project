from django.shortcuts import render
from django.utils import is_valid_file_path, is_valid_url, process_csv_

# Create your views here.

def index (request):
    return render(request,"index.html") 
#return HttpResponse("this is homepage")
    
def run_task(request):
  if request.method == 'POST':
    path_url = request.POST.get('path_url')
    task_name = request.POST.get('Task1_Path')  # Assuming task name is also submitted

    if is_valid_file_path(path_url) or is_valid_url(path_url):
      # Path/URL is valid, proceed with task dispatch

      process_csv.delay(path_url)
      #task = get_task_by_name(task_name)  # Retrieve the Celery task function
      #task.delay(path_url)  # Dispatch the Celery task asynchronously

      context = {'result_message': 'Task dispatched successfully.'}
      return render(request, 'index.html', context)
    else:
      # Path/URL is invalid, update context with error message
      context = {'error_message': 'Invalid path or URL provided.'}
      return render(request, 'index.html', context)
  else:
    # Handle GET requests (optional, e.g., display initial form)
    return render(request, 'index.html')
  
