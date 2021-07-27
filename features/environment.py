import os
import tempfile
from behave import fixture, use_fixture
from flaskr import create_app
from db import init_db

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait

@fixture
def flaskr_client(context, *args, **kwargs):
    app = create_app()
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.testing = True
    context.client = app.test_client()
    with app.app_context():
        init_db()
    yield context.client
    # -- CLEANUP:
    os.close(context.db)
    os.unlink(app.config['DATABASE'])

def before_feature(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(flaskr_client, context)
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(context.browser, 10)

def after_feature(context, feature):
    context.browser.quit()