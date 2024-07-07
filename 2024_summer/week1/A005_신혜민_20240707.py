'''
A005 - 스킬트리
skill(String), skill_trees(String[] skill_trees)가 매개변수로 주어진다. skill 순서에 맞는 skill_trees의 개수를 return하는 함수를 작성한다.
'''
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        filtered = ''.join([s for s in skill_tree if s in skill])
        if skill.startswith(filtered):
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))  
