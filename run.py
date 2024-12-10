import webbrowser
from app import create_app

# Create the app instance
app = create_app()

# Open the browser automatically on app startup
if __name__ == '__main__':
    # Open the browser to the welcome route
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)
