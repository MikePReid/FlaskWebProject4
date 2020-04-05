import os
from HelloFlask import app    # Imports the code from HelloFlask/__init__.py

# ref: https://docs.microsoft.com/en-us/visualstudio/python/learn-flask-visual-studio-step-01-project-solution?view=vs-2019

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)
