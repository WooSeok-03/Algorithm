def solution(nums):
    pon = list(set(nums))
    case = int(len(nums) / 2)
    
    if len(pon) >= case:
        return case
    else:
        return len(pon)

# 중복을 제거한 nums의 길이와 nums길이/2 중에서 최솟값을 return 
#def solution(nums):
#    return min(len(nums)/2, len(set(nums)))