from string import ascii_uppercase
from string import ascii_lowercase
import collections

Plaintext_dict = {}
Ciphertext_dict = {}
k = 0

tmp_list = list()
freq_list = list()

for i in ascii_lowercase:
    Plaintext_dict[i] = k
    k += 1

k = 0

for i in ascii_uppercase:
    Ciphertext_dict[i] = k
    k += 1

k = 0

reverse_Plain = dict(map(reversed, Plaintext_dict.items()))
reverse_Cipher = dict(map(reversed, Ciphertext_dict.items()))

my_list = input().strip()  #입력
print('입력된 암호문 :', my_list)

print(' ')
answer = collections.Counter(my_list)
values = [i for i in answer.values()]

values.sort(reverse=True)  # 큰 수 부터 배열

for m in range(5):
    big = values[m]  # 첫번째 원소가 가장 많이 나온 빈도수

    freq_result = [i for i, k in answer.items() if big == k]
    # range의 items를 꺼내 i, k에 넣고 k==big인 경우 i를 result list에 넣는다.
    freq_result = ''.join(sorted(freq_result))  #사전순 정렬
    tmp_list.append(freq_result)


for v in tmp_list:
    if v not in freq_list:
        freq_list.append(v)

strTmp = "".join(freq_list)
freq_list = list(strTmp)

print('출현 빈도 수', freq_list)

for t in range(len(freq_list)):
    k = 0
    key = Ciphertext_dict.get(freq_list[t])-4 # 가장 많이 나온 알파벳을 E로 가정, 4를 빼준다.
    print('key', key, ' : ', end='')

    for i in my_list:
        print(reverse_Plain.get((Ciphertext_dict.get(my_list[k]) - key) % 26), end='')
        k += 1

    print('')
