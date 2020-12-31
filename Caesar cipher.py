'''
시저 암호 (Caesar cipher)
글자의 순서를 일정 간격으로 밀어서 치환하는 암호화 방식
'''

# 프로그래머스 시저암호 문제

# n 만큼 뒤로 밀어서 치환
# 대문자인 경우
alp.isupper():
    chr((ord(alp) - ord('A') + n)%26 + ord('A'))

# 소문자인 경우
alp.islower():
    chr((ord(alp) - ord('a') + n) % 26 + ord('a')