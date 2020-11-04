from flask import Flask, render_template, session, g
from datetime import datetime
import view, os

database = None
app_global = None

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.add_url_rule('/login', view_func=view.login, methods=['GET' , 'POST'])
    app.add_url_rule('/profile', view_func=view.profile)
    app.add_url_rule('/logout', view_func=view.logout)
    app.add_url_rule('/register', view_func=view.register, methods=['GET' , 'POST'])
    app.add_url_rule('/', view_func=view.home)
    app.before_request(view.before_request)
    app.config.from_object('settings')
    return app


        
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080)



