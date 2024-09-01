"""
https://school.programmers.co.kr/learn/courses/30/lessons/250121
프로그래머스 - PCCP 기출문제 <데이터 분석>

데이터 구성 
["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
data - 정렬한 데이터들이 담긴 이차원 정수 리스트
ext - 떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열
val_ext - 뽑아낼 정보의 기준값을 나타내는 정수 
sort_by가 - 정보를 정렬할 기준이 되는 문자열
data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return 하도록 solution 함수를 완성 !!!
"""

def solution(data, ext, val_ext, sort_by):
    ext_index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}[ext]
    sort_by_index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}[sort_by]
    
    filtered_data = [row for row in data if row[ext_index] < val_ext]
    
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_by_index])
    
    return sorted_data

"""
data - 이차원 정수 리스트
ext - 어떤 정보를 기준으로 데이터를 뽑아낼지 의미
val_ext - 뽑아낼 정보의 기준값
sort_by - 정보를 정렬할 기준이 되는 문자열
"""
