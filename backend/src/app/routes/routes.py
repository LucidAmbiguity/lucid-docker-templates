"""Main Routes File for the Project"""


from app.routes import routes  # type: ignore[no-redef] # pylint: disable=import-self

# ! Theses can probably all go away

@routes.route('/') # type: ignore[attr-defined,misc]
@routes.route('/index') # type: ignore[attr-defined,misc]
def index() ->str:
    """
    Home Page
      - Junk data for proof of works
    """
    
    result = {
      "user" : {'username': 'Rufus'},
      "posts" : [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
      ]
    }
    return result

