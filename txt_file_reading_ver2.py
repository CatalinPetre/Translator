

my_dict = {}
my_word_list = []
my_sentance_list = []
with open('wortliste_test1.txt', mode = 'r') as txt_file:
	for line in txt_file:
		my_line = line.split(None, 1)
		first_word = my_line[0]
		if first_word == 'der' or first_word == 'die' or first_word == 'das':
			my_line = line.split(None, 2)
			first_word = my_line[0:2]
			first_word = first_word[0] + ' ' + first_word[1]
		my_word_list.append(first_word)

		# if len(my_line) > 1:
		# 	sentance = my_line[1]
		# 	print(sentance)
		# 	my_sentance_list.append(sentance)

		
		#print(type(first_word))
		#my_dict = dict({first_word:sentance})
		#my_dict[first_word] = sentance
	#print(my_dict)
	print(my_word_list)
	print(my_sentance_list)

print (len(my_word_list))


#my_string = 'Köln'
#my_string = my_string.decode('ansi')	
#print(my_string)
		#print(type(item))
		#my_word_list.append(item)
	
	#print(my_worda_list) 

