VOWELS = 'aeiou'

def is_acceptable(password):
    has_vowel = False
    vowel_count = 0
    consonant_count = 0

    for i in range(len(password)):
        if password[i] in VOWELS:
            has_vowel = True
            vowel_count += 1
            consonant_count = 0 # 자/모음 연속 해제
        else:
            consonant_count += 1
            vowel_count = 0 # 자/모음 연속 해제

        if vowel_count == 3 or consonant_count == 3: # 자/모음 연속 판별(2번)
            return False

        if i > 0:
            if password[i] == password[i-1] and password[i] not in 'eo': # 문자 연속 판별(3번)
                return False

    if not has_vowel: # 자음 여부 판별(1번)
        return False

    return True

while True:
    password = input()
    if password == 'end':
        break
    if is_acceptable(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
