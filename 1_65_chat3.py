"""
1. 解釋程式目標
2. 寫程式碼來讀取檔案
3. 解釋字串的切割(把字串中的一部分取出)
4. 建立版本上傳

"""
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # \ufeff: txt, word等軟體存檔時偷存的編碼資料，以encoding='utf-8-sig'編碼去除
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	for line in lines:
		s = line.split(' ')
		time = s[0][:5]
		name = s[0][5:]
		print(name)

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('3.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)
	
main()