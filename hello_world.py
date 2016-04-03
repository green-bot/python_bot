import json
import os
import sys

def say(prompt):
    print prompt
    sys.stdout.flush()

def ask(prompt):
    say(prompt)
    return raw_input()

PROMPT_1 = os.getenv('PROMPT_1', 'Prompt 1 default') + "\n"
say(PROMPT_1)
answer = ask("Give me something to say")
say("You said: " + answer)
collected_d = dict()
collected_d['answer'] = answer
say(json.dumps(collected_d))
