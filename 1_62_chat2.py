"""
1. 解釋程式目標
2. 修改convert function
3. 解釋split()的結果，我們想拿到"所有s[2]以後的東西"，因為那部分才是對話紀錄

"""
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # \ufeff: txt, word等軟體存檔時偷存的編碼資料，以encoding='utf-8-sig'編碼去除
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None 
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)	
	print('Allen說了', allen_word_count, '個字')
	print('Allen傳了', allen_sticker_count, '個貼圖')
	print('Allen傳了', allen_image_count, '個圖片')
	
	print('Viki說了', viki_word_count, '個字')
	print('Viki傳了', viki_sticker_count, '個貼圖')
	print('Viki傳了', viki_image_count, '個圖片')

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)
	
main()