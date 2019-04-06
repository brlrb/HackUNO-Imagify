from app import app

@app.route('/')
def root():
    return "Page load works"




