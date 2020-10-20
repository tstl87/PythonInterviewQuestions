from enum import Enum

class DigitState(Enum):
	BEGIN = 0
	NEGATIVE1 = 1
	DIGIT1 = 2
	DOT = 3
	DIGIT2 = 4
	E = 5
	NEGATIVE2 = 6
	DIGIT3 = 7
		
digit_lambdas = {
	DigitState.BEGIN: lambda x: True,
	DigitState.NEGATIVE1: lambda x: x == '-',
	DigitState.DIGIT1: lambda x: x.isdigit(),
	DigitState.DOT: lambda x: x == '.',
	DigitState.DIGIT2: lambda x: x.isdigit(),
	DigitState.E: lambda x: x == 'e',
	DigitState.NEGATIVE2: lambda x: x == '-',
	DigitState.DIGIT3: lambda x: x.isdigit()
	}

fsm = {
	DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1, DigitState.DOT],
	DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
	DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
	DigitState.DOT: [DigitState.DIGIT2],
	DigitState.DIGIT2: [DigitState.DIGIT2, DigitState.E],
	DigitState.E: [DigitState.DIGIT3, DigitState.NEGATIVE2],
	DigitState.NEGATIVE2: [DigitState.DIGIT3],
	DigitState.DIGIT3: [DigitState.DIGIT3]
	}

def parse_number(s):
	state = DigitState.BEGIN
		
	for ch in s:
		found_next_state = False
		for next_state in fsm[state]:
			if digit_lambdas[next_state](ch):
				state = next_state
				found_next_state = True
				break
						
		if not found_next_state:
			return False
				
	#return state in (DigitState.DIGIT1, DigitState.DIGIT2, DigitState.DIGIT3)
	return state in (DigitState.DIGIT1, DigitState.DIGIT2, DigitState.DIGIT3)

print(parse_number("12.35"))
# True

print(parse_number("12.35"))
# True

print(parse_number("12a"))
# False