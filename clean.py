text_out = []

with open('landmark_test.txt') as f1:
	for line in f1:
		line_list = line.split(' ')
		l = [line_list[0]]
		text_out.append(l+line_list[6:])
with open('keypoint_test.txt','w') as f:
	for i in text_out:
		s = i[0]
		for p in i[1:]:
			s += ' '
			s += p
		f.write(s)