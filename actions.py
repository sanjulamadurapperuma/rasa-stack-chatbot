# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import IPython
from IPython.display import clear_output, HTML, display
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

interpreter = RasaNLUInterpreter('models/current/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('models/current/dialogue', interpreter=interpreter)


def run(self, dispatcher, tracker, domain):
    # what your action should do
    dispatcher.utter_message(messages)  # send the message back to the user
    return []


while True:
    clear_output()
    display(run(messages))
    time.sleep(0.3)
    a = input()
    messages.append(a)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for r in responses:
        messages.append(r.get("text"))

