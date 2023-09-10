from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

# initializing Flask in app.py
app = Flask(__name__)
# Session Key config
app.config['SECRET_KEY'] = 'secret'
# Will not run debugger
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.debug = True
toolbar = DebugToolbarExtension(app)


# importing Boggle game
boggle_game = Boggle()







# vvvvvvvvvvvvvvvvv CODE vvvvvvvvvvvvvvvvvvvvvvv







@app.route('/')
def home():
    """Home Page with Board and Word Form"""


    board = boggle_game.make_board()
    session['board'] = board # establish a session to be accessible within the file
    if 'highestscore' not in session:
        session['highestscore'] = 0
    return render_template('home.html', board=board)



@app.route('/verify-word', methods=['POST'])
def check_word():
    """Server checks word and prompts response back to AJAX"""

    word = request.get_json().get('word','') # 1) retrieve word from AJAX request
    board = session.get('board', []) # 1.5) retrive board from session
    result = boggle_game.check_valid_word(board, word) # 2) retrieve returned msg from function

    return jsonify(result=result) # transforming and returning a JSON response



@app.route('/finalized', methods=['POST'])
def finalized():
    """Finalizing game by retrieving score and no. of tries and storing in session"""


    session['score'] = request.get_json().get('scoreCount','')
    session['tries'] = request.get_json().get('tries','')
    highest_score = request.get_json().get('highestScore', 0)
    session['highestscore'] = max(session.get('highestscore', 0), highest_score)


    return jsonify(result='End of Game', score=session['score'], tries=session['tries'])



@app.route('/end-of-game', methods=['GET'])
def end_of_game():
    """Redirecting user to /end-of-game page after the window.href line in JS"""

    score = session.get('score',0)
    tries = session.get('tries',0)
    highestscore = session.get('highestscore', 0)
    return render_template('endgame.html', score=score, tries=tries, highestscore=highestscore)