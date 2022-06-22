# Python_encryption


## Additional_Cipher.py
대칭 덧셈 암호 해독 프로그램 (통계 공격)
가장 빈번히 나타나는 단어 5개를 각각 ‘E’로 변환한 결과를 출력하는 파이썬 프로그램

테스트 암호문 : 
RVJZJSRJVUFERUVJZXEGIZETZGCVBEFNERJRJLSJKZKLKZFEGVIDLKRKZFEEVKNFIBREUZJVWWZTZVEKZESFKYJFWKNRIVREUYRIUNRIV


## bitcoin_key_convert.py

비트코인의 개인키를 16진수로 입력받아, 공개키를 16진수로 출력하는 파이썬 프로그램

비트코인의 공개 키는 아래와 같은 SECP256K1 타원 곡선을 이용

Y2 = (X3 + 7) % p
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

개인키가 x라고 하면 공개 키는 x * G의 결과로 생성되는데, G는 타원 곡선상의 고정된 점으로 좌표는 다음과 같다.

G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)


곱셈 역원 계산은 Extended Euclidian 알고리즘, 곱하기 연산은 double-and-add 알고리즘을 이용.


아래는 테스트를 위한 개인키와 공개키.

개인키: 3

공개키: ( 	0xf9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9,
			0x388f7b0f632de8140fe337e62a37f3566500a99934c2231b6cb9fd7584b8e672 )

개인키: 0x1e99423a4ed27608a15a2616a2b0e9e52ced330ac530edcc32c8ffc6a526aedd

공개키: (	0xf028892bad7ed57d2fb57bf33081d5cfcf6f9ed3d3d7f159c2e2fff579dc341a, 
			0x7cf33da18bd734c600b96a72bbc4749d5141c90ec8ac328ae52ddfe2e505bdb )
