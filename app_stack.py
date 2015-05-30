stack = []
def add(pos, value):

	stack[pos] = value

	if (stack[pos] == value):
		return True
	else:
		return False


def pop(pos):
	stack[pos]   = 0 	#0 == null
	if (stack[pos] == 0):
		return True
	else:
		return False

def get(pos):


	get = stack[pos] 

	if (get == stack[pos] and get != null):


		return get
	else:
		return 0  # 0 is an error
