from cryptography.fernet import Fernet

f1 = open("data.txt", 'r')
lines = f1.readlines()
f1.close()
print('data.txt 의 내용 :', lines)

PlainText = ''.join(lines).encode()

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(PlainText)

CipherText = str(token, 'utf-8')
print('암호화 결과 :',CipherText)

f2 = open("encrypt.txt", 'w')
f2.write(CipherText)
f2.close()

print('암호화 파일 저장 Ok...')

f1 = open("encrypt.txt", 'r')
lines = f1.readlines()
f1.close()
print('암호화 파일 불러오기 Ok...')

CipherText = ''.join(lines).encode()

PlainText = f.decrypt(CipherText)
print('불러온 파일 해석 결과 :', PlainText)