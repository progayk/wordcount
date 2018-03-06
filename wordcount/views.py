from django.shortcuts import render
from django.http import HttpResponse
import operator


def index(request):
	# return render()
	return render(request, 'index.html', {'hithere': 'hey this is me!'})


def cokyakinda(request):
	return render(request, 'cokyakinda.html')


def about(request):
	return render(request, 'about.html')


def count(request):
	fulltext = request.GET['fulltext']

	words_list = fulltext.split()

	word_dict = {}
	for word in words_list:
		if word in word_dict:
			#increase the number
			word_dict[word] += 1
		else:
			#add to dict
			word_dict[word] = 1

	#sort the values reverse
	sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext': fulltext,
		'count': len(words_list),
		'sorted_dict': sorted_dict})