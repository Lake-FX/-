import re

f = open("llyc.txt","r",encoding="utf-8")
data = f.readlines()
f.close()

#parallel [ˈpærəlel]

# adj. 平行的；并联的；相同的，类似的

# n. 平行线；比拟；相似处；纬线

# v. 与…相似

# 记

#将所有信息组成一个字符串
data_str = ''
for word in data:
	data_str = data_str + word

#第一步正则获取每个单词和单词的意思词组
pattern_res = re.findall(r'[a-zA-Z]+\(?[a-zA-Z]*?\)?[a-zA-Z]*?\s\[.*?\]\n\n(?:[a-zA-Z]+\..*?\n\n)+',data_str)

#获取单元

#再次拼接所有字符串
dict_res = {}

for words in pattern_res:
	deal1 = words.replace("\n\n","\n")
	word_deal = re.findall(r'([a-zA-Z]+\(?[a-zA-Z]*?\)?[a-zA-Z]*?)\s\[',deal1)[0]
	deal2 = re.findall(r'(?:[a-zA-Z]+\..*?\n+)+',deal1)[0]
	#分割
	deal3 = deal2.split('\n')[:-1]

	#去除重复项
	if len(deal3) == 1:
		#表示无重复
		pass
	else:
		
		#大于一项判断是否有重复,第一项和最后一项词性是否相同n v adj adv
		first_ = re.findall(r'[a-zA-Z]+\.',deal3[0])[0]
		last_ = re.findall(r'[a-zA-Z]+\.',deal3[-1])[0]
		
		#如果词性相同就去掉最后一个
		if first_==last_:
			deal3 = deal3[:-1]

	#取最后一个和前面所有的进行比较
	deal4 = ''
	for str_  in deal3:
		deal4 = deal4 +  str_  + '\n'
	#将deal组合起来
	dict_res[word_deal] = deal4[:-1]
#print(dict_res)
#将信息写入js文件
#构造文本
write_text = "\nvar trans_list = " + str(dict_res)

#写入js文件
with open('word.js', 'a') as f:
	f.write(write_text)
	f.close()