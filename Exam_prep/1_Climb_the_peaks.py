from collections import deque

conquered_peaks = []

food_portions = [int(x) for x in input().split(', ')]
stamina = deque([int(x) for x in input().split(', ')])

peaks = {
    80: "Vihren",
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza",
}

while food_portions and stamina:
    current_portion = food_portions.pop()
    current_stamina = stamina.popleft()
    result = current_portion + current_stamina

    for points, peak in peaks.items():
        if result >= points:
            conquered_peaks.append(peaks.pop(points))
        break

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep='\n')

