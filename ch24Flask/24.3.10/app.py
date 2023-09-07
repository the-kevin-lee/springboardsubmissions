from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, Question, satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True
toolbar = DebugToolbarExtension(app)


responses = []


@app.route('/')
def home_page():
    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    return render_template('root.html', survey_title=survey_title, survey_instructions=survey_instructions,)


# create the dynamic route for handling different questions with the satisfaction_survey.questions list
@app.route('/questions/<int:questid>', methods=['GET', 'POST'])
def question(questid):
    # for when the user tries to manually enter a different question number
    if questid != len(responses):
        # allowing user to go back to a previous question already answered
        if questid < len(responses):
            return redirect(f'/questions/{questid}')
        # checks if user is trying to access another question that is valid because it is within the range of questions
        elif questid > len(responses) and questid < len(satisfaction_survey.questions):
            flash("You are accessing the wrong question!")
            return redirect(f'/questions/{len(responses)}')
        # check if the user had already completed the survey but tries to access a questid out of range
        elif questid > len(satisfaction_survey.questions) - 1 and len(responses) == len(satisfaction_survey.questions):
            return redirect('/thanks')
        # check if the user had not completed the survey and tries to access a questid out of range
        elif questid > len(satisfaction_survey.questions) - 1 and len(responses) != len(satisfaction_survey.questions):
            flash("What are you doing?")
            return redirect(f'/questions/{len(responses)}')

    # First check if the method is POST
    if request.method == 'POST':
        # appending answers to the responses list
        answer = request.form['answer']
        responses.append(answer)

        nextquestid = questid + 1
        if nextquestid < len(satisfaction_survey.questions):
            return redirect(f"/questions/{nextquestid}")
        else:
            return redirect('/thanks')  # redirecting to a thank you page

    # accessing current question and choices data
    thequestion = satisfaction_survey.questions[questid].question
    thechoices = satisfaction_survey.questions[questid].choices
    return render_template('question.html', thequestion=thequestion, thechoices=thechoices)


# create a route for thanks.html
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')
