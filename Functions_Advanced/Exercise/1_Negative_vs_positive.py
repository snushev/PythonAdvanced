def checker(lst):
    positive = [x for x in numbers if x > 0]
    negative = [x for x in numbers if x < 0]

    print(sum(negative))
    print(sum(positive))

    if sum(positive) > abs(sum(negative)):
        return "The positives are stronger than the negatives"
    elif sum(positive) < abs(sum(negative)):
        return "The negatives are stronger than the positives"


numbers = list(map(int, input().split()))



print(checker(numbers))