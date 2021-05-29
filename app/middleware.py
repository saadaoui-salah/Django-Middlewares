class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_exceptions = 0
        self.context_response = {
            "msg": {"warning": "Hello from context response !"}
        }

    def __call__(self, request):
        print("MIDDLEWARE CALLED")
        response = self.get_response(request)
        return response
        
    def process_template_response(self, request, response):
        response.context_data['new_data'] = self.context_response
        print(self.context_response)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # executing before call view
        # give acces to the view & arguments
        print(f'view name: {view_func.__name__} ')
        pass

    def process_exception(self, request, exception):
        self.num_exceptions += 1
        print(f"exceptions number: {self.num_exceptions}")
        pass
