

from django_middlewares.settings import MIDDLEWARE


class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("MIDDLEWARE CALLED")
        response = self.get_response(request)
        return response