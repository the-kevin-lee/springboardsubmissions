
# importing unittesting for unit tests and integration tests
from unittest import TestCase
# importing app file (that has the view funcs)
from app import app
# imports session from flask
from flask import session, json
# importing Boggle class from Boggle
from boggle import Boggle


# vvvvvvvvvvvvvvv IMPORTANT TO CONFIG WHEN TESTINGvvvvvvvvvvvvvvv

# Make Flask errors be real Python errors, not HTML pages with error info
app.config['TESTING'] = True

# not to use the debug toolbar when testing 
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!


    # vvvvvvvvvvv SET UP AND TEAR DOWN  vvvvvvvvvvvvvvvv
    def setUp(self):
        """Test client set up with session variables"""
        self.client = app.test_client()
        with self.client.session_transaction() as session:
            session['board'] = [
                ['A', 'B', 'C', 'D', 'E'],
                ['F', 'G', 'H', 'I', 'J'],
                ['K', 'L', 'M', 'N', 'O'],
                ['P', 'Q', 'R', 'S', 'T'],
                ['U', 'V', 'W', 'X', 'Y']
            ]


    

    # vvvvvvvvvvvvvvvv TEST FUNCS vvvvvvvvvvvvvvvvvvvvv
    # View Func 1)
    def test_load_home(self):
        """checks for home.html to load correctly with correct content"""
        with app.test_client() as client:

            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Welcome to the Boggle Game!</h1>',html)


    #View Func 2)
    def test_guess(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [['H', 'I'], ['A', 'B']]  # Mocking a 2x2 board with the word "HI"
            
            payload = json.dumps({"word": "hi"})
            resp = client.post('/verify-word', data=payload, content_type='application/json')
            data = json.loads(resp.get_data(as_text=True))

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(data['result'], 'ok')  # Assuming 'hi' is a valid word in both dictionary and board

    
    #View Func 3)
    def test_finalized(self):
        with app.test_client() as client:

            payload = json.dumps({
                'scoreCount': 10,
                'tries': 5,
                'highestScore': 15
            })
            response = client.post('/finalized',data=payload,content_type='application/json')
            data = json.loads(response.get_data(as_text=True))

            self.assertEqual(response.status_code,200)
            assert data['result'] == 'End of Game'
            assert data['score'] == 10
            assert data['tries'] == 5


    #View Func 4)
    def test_end_of_game(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['score'] = 10
                sess['tries'] = 5
                sess['highestscore'] = 15

            response = client.get('/end-of-game')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Your Final Score is...</h1>', html)
            self.assertIn('<h2>After ..</h2>', html)
            self.assertIn('<h2>Your Highest Score So Far is 15</h2>', html)
           


