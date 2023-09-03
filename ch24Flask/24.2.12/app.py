from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story
from random import * 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'







# vvvvvvvvvvvvvvvvvvvv CODE vvvvvvvvvvvvvvvvvvvvvvvv


@app.route('/')
def add_story():
    return render_template('form.html')


@app.route('/new-story')
def new_story():
    answers = {}
    prompts = ['noun', 'verb', 'adjective', 'plural_noun', 'place']

    for prompt in prompts:
        answer = request.args.get(prompt)
        if answer:  # Only add to answers if the answer is not None
            answers[prompt] = answer

    story = request.args.get('story')
    final = Story(prompts, story)
    generated_story = final.generate(answers)

    return render_template('new_story.html', generated_story=generated_story)
