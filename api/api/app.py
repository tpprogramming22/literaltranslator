from django.http import JsonResponse
from django.middleware import csrf
from .main import translating_function

def hello(request):
    if request.method == 'POST':
        data = request.POST.get('data', '')
        # modified_data = data[::-1]  # Reverse the string
        # response_data = {
        #     'message': 'Data reversed successfully',
        #     'modified_data': modified_data
        # }

        input = translating_function(data)
        print(input)
        response_data = {
            'message': input
        }


        return JsonResponse(response_data)
    else:
        csrf_token = csrf.get_token(request)
        response_data = {
            'message': 'Please send a POST request with "data" parameter',
            'csrf_token': csrf_token
        }
        return JsonResponse(response_data)
