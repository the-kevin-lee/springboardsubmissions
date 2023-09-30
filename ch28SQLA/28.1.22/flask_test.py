from unittest import TestCase

from factory import factory
from models import db, Users


factory.config['SQLALCHEMY_DATABASE-URI'] = 'postgresql:///factory-flask-test'
factory.config['SQLALCHEMY_ECHO'] = False


factory.config['TESTING'] = True
factory.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']



db.drop_all()
db.create_all()






class UsersTestCase(TestCase):
    """Test Users View Funcs """

    def setUp(self):
        """Add sample User"""
        Users.query.delete()
        test_User = Users(first_name='Michael', last_name='Scott', image_url='some_image_url')
        db.session.add(test_User)
        db.session.commit()
        self.user_id = test_User.id  # Store the ID for later use

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.session.rollback()

    
    def test_list_users(self):
        with factory.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Michael', html)

    
    def test_show_user_details(self):
        with factory.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")  
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Michael Scott</h1>', html)

   
    def test_add_user(self):
        with factory.test_client() as client:
            u = {"first_name": "Dwayne", "last_name": "Johnson", "image_url": "some_other_image_url"}
            resp = client.post("/users/new", data=u, follow_redirects=True)  # Adjust URL as needed
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Dwayne", html)

    def test_edit_user(self):
        with factory.test_client() as client:
            u = {"first_name": "UpdatedName", "last_name": "UpdatedLast", "image_url": "updated_image_url"}
            resp = client.post(f"/users/edit/{self.user_id}", data=u, follow_redirects=True)  # Use stored user ID
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("UpdatedName", html)



    