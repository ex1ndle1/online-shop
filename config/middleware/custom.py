class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('Мы только начали')


    def __call__(self, request):
        print('это мд до view')
        response = self.get_response(request)
        print('это после')
        return response
