# 문제 3
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.
word_dict = {}



s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
s = s.upper().replace(',', '').replace('.', '').replace('\n','').split(' ')
s_list = list(set(s))
s_list.sort(key=str)

print(s)
print(s_list)

for item in s:
    count = word_dict.get(item, 0)
    word_dict[item] = count + 1

for words in word_dict:
    print(words, word_dict[words])


