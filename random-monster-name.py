import textwrap, random

class NameGenerator(object):

	with open('txt/namegenerator/name.txt', 'r') as f:
    	names = f.read().splitlines()
   		random.shuffle(names)

	with open('txt/namegenerator/pre.txt', 'r') as f:
   	 	pre = f.read().splitlines()

	with open('txt/namegenerator/adjective.txt', 'r') as f:
    	adjectives = f.read().splitlines()
    	random.shuffle(adjectives)

	with open('txt/namegenerator/type.txt', 'r') as f:
   		types = f.read().splitlines()
    	random.shuffle(types)

	with open('txt/namegenerator/objective.txt', 'r') as f:
    	objectives = f.read().splitlines()
   		random.shuffle(objectives)

	def getName (self):
		combined = zip(names,pre,adjectives,types,objectives)
		return combined[1]

	#print ' '.join(combined[1])
