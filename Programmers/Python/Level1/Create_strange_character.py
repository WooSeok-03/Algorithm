def solution(s):
    answer = ''
    count = 0
    
    str_list = list(s)
    
    for i in range(len(list(s))):
        if str_list[i] == " ": 
            count = 0
            continue
            
        if count % 2 == 0:
            str_list[i] = str(str_list[i]).upper()
        else:
            str_list[i] = str(str_list[i]).lower()
        count += 1
    
    return "".join(str_list)