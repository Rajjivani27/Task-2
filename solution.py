def solution(ratings)-> int:
    size = len(ratings)

    if size == 1:
        return 1
    
    ans = 0
    
    for i in range(0,size):
        if i == 0:
            if ratings[i] > ratings[i+1]:
                ans += 2
            else:
                ans += 1
        elif i==size-1:
            if ratings[i] > ratings[i-1]:
                ans += 2
            else:
                ans += 1
        else:
            if ratings[i] > ratings[i-1] or ratings[i] > ratings[i+1]:
                ans += 2
            else:
                ans += 1

    return ans

n = int(input("Enter the size of list: "))
ratings = []

for i in range(0,n):
    num = int(input("Enter the rating: "))
    ratings.append(num)

ans = solution(ratings)

print(f"Required Candies = {ans}")


