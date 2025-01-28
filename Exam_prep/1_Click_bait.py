from collections import deque

suggested_links = deque(map(int,input().split()))
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())
final_feed = []

while suggested_links and featured_articles:
    first_element = suggested_links.popleft()
    second_element = featured_articles.pop()

    if second_element > first_element:
        result = second_element % first_element
        final_feed.append(abs(result))
        result *= 2
        if result != 0:
            featured_articles.append(result)
    elif first_element > second_element:
        result = first_element % second_element
        final_feed.append(-result)
        result *= 2
        if result != 0:
            suggested_links.append(result)
    else:
        final_feed.append(0)

total_engagement_value = sum(final_feed)


print(f"Final Feed: {', '.join(map(str,final_feed))}")

if total_engagement_value < target_engagement_value:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")
else:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")

