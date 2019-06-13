#
# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을
# 분리하여 출력하세요.

s = '/usr/local/bin/python'

full_dir = s.split('/')[1:]
dirname = s.rsplit('/', 1)
filename = dirname[1]

print(full_dir)
print(dirname)
print(filename)
