def solution(participant, completion):
    answer = ''
    for i in range(len(participant)):
        for j in range(len(completion)):
            if completion[j] == participant[i]:
                del completion[j]
            else:
                answer += participant[i]
    return answer
