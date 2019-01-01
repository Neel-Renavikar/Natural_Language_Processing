import sys
import json
from pprint import pprint

with open('../Automata_models/SheepTalk.json') as f:
	data = json.load(f)

input_string = sys.argv[1]
accepted = 0
rejected = 0

for state in data["Starting_states"]:
	if accepted == 0:
		current_state = state["id"].encode('ascii','ignore')
		next_state = current_state ##Placeholder
		for char in input_string:
			if rejected == 0:
				checked = 0
				for func in data["Transition_functions"]:
					if checked ==0:
						if (current_state == func["state"].encode('ascii','ignore') and checked == 0):
							passed = 0
							for charfunc in func["function"]:
								if (char == charfunc["input_char"].encode('ascii','ignore') and checked == 0):
									next_state = charfunc["next_state"].encode('ascii','ignore')
									passed = 1
									checked = 1
							if passed == 0:
								rejected = 1
				if checked == 0:
					rejected = 1
			if rejected == 0:
				current_state = next_state
		isInFinalState = 0
		for accepting_state in data["Accepting_states"]:
			if isInFinalState == 0 and current_state == accepting_state["id"].encode('ascii','ignore'):
				isInFinalState = 1
		if rejected == 0 and isInFinalState == 1:
			accepted = 1
if accepted == 1:
	print("accepted")
else:
	print("rejected")