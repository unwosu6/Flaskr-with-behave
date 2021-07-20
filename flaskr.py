import os

from flask import Flask
from flask_behind_proxy import FlaskBehindProxy
from db import close_db, init_db_command
from auth import bp
import blog


app = Flask(__name__, instance_relative_config=True)
proxied = FlaskBehindProxy(app)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

app.teardown_appcontext(close_db)
app.cli.add_command(init_db_command)
app.register_blueprint(bp)
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")