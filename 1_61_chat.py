"""
1. 建立GitHub專案
2. 解釋程式目標
3. 寫讀取檔案function
4. 寫main function
5. [主要]寫 轉換function
6. 介紹None出場
7. 寫 寫入檔案function

"""
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # \ufeff: txt, word等軟體存檔時偷存的編碼資料，以encoding='utf-8-sig'編碼去除
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None #如果對話紀錄第一行不是人名，程式會當掉，預防此風險的作法
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值的意思
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)
	
main()