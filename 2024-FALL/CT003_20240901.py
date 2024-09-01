"""
https://school.programmers.co.kr/learn/courses/30/lessons/178871
프로그래머스 - <달리기 경주>

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성 !! 
"""

def solution(players, callings):
    player_indices = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = player_indices[call]
        if idx > 0:
            players[idx], players[idx-1] = players[idx-1], players[idx]
            player_indices[players[idx]] = idx
            player_indices[players[idx-1]] = idx - 1
            
    return players
