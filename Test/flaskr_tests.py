import os
# import flaskr
import views 
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.register = register()
        # self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        # flaskr.app.testing = True
        # self.app = flaskr.app.test_client()
        # with flaskr.app.app_context():
            # flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_create_account(self, username, email, fullname, password):
        return self.register.post('/register', data=dict(
            username=username,
            fullname = fullname,
            email = email,
            password = password,
            ))


if __name__ == '__main__':
    unittest.main()