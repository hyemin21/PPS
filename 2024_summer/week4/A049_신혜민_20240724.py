"""
A049 - https://www.acmicpc.net/problem/4659
"""
# 문제 4659
def problem_4659(passwords):
    def is_acceptable(password):
        vowels = set('aeiou')
        has_vowel = any(char in vowels for char in password)
        if not has_vowel:
            return False

        for i in range(len(password) - 2):
            if (password[i] in vowels and password[i+1] in vowels and password[i+2] in vowels) or \
               (password[i] not in vowels and password[i+1] not in vowels and password[i+2] not in vowels):
                return False

        for i in range(len(password) - 1):
            if password[i] == password[i+1] and password[i] not in 'eo':
                return False

        return True

    results = []
    for password in passwords:
        if is_acceptable(password):
            results.append(f"<{password}> is acceptable.")
        else:
            results.append(f"<{password}> is not acceptable.")
    return results

