from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def hello():
    data = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidate_list=data)


@app.route('/candidate/<int:x>')
def candidate_id(x):
    i = get_candidate(x)
    return render_template('card.html', user=i)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    i = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidate_list_name=i, candidates_len=len(i))


@app.route('/skills/<skill>')
def search_skills(skill):
    i = get_candidates_by_skill(skill)
    return render_template('skill.html', candidate_list_skill=i, candidates_len=len(i), skill=skill)


app.run()

