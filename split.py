text_train = []
text_test  = []

with open('finaltest.txt') as f1:
	for line in f1:
		if 'train' in line:
			text_train.append(line)
		elif 'test' in line:
			text_test.append(line)

with open('finaltrain.txt') as f2:
	for line in f2:
		if 'train' in line:
			text_train.append(line)
		elif 'test' in line:
			text_test.append(line)

with open('landmark_train.txt','w') as f:
	for i in text_train:
		f.write(i)
with open('landmark_test.txt','w') as f:
	for i in text_test:
		f.write(i)