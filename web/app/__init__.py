from flask import Flask, session
from automlk.print import *

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object('config')
app.jinja_env.globals.update(print_list=print_list)
app.jinja_env.globals.update(print_score=print_score)
app.jinja_env.globals.update(print_score_std=print_score_std)
app.jinja_env.globals.update(print_value=print_value)
app.jinja_env.globals.update(print_duration=print_duration)
app.jinja_env.globals.update(print_params=print_params)
app.jinja_env.globals.update(print_other_metrics=print_other_metrics)

from app import views