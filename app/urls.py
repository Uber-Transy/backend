from .views import UserAPI, PostAPI

def register_routes(app):
    # Register the UserAPI and PostAPI as class-based views
    app.add_url_rule('/users', view_func=UserAPI.as_view('user_api'))
    app.add_url_rule('/posts', view_func=PostAPI.as_view('post_api'))
