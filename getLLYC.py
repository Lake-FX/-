import re

f = open("llyc.txt","r",encoding="utf-8")
data = f.readlines()
f.close()

find_list = ''
for word in data:
	pattern_res = re.findall(r'[a-zA-Z]*?\s\[',word)
	pattern_unit = re.findall(r'Unit\s\d\d',word)
	if len(pattern_res)>0:
		the_word = pattern_res[0][:-2]
		if(len(the_word)>1):
			find_list = find_list +  the_word + ","
	if len(pattern_unit)>0:
		find_list = find_list + "day"
split1 = find_list[90:].split("day")

res_list = []
for one_day in split1[1:]:
	split2 = one_day.split(",")[:-1]
	res_list.append(split2)
#构造文本
write_text = "var word_list = " + str(res_list)

#写入js文件
with open('word.js', 'w') as f:
	f.write(write_text)
	f.close()


