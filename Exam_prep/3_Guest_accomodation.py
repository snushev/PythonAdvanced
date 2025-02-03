def accommodate(*args, **kwargs):
    sorted_rooms = sorted(((int(k.split('_')[1]), v) for k, v in kwargs.items()), key=lambda x: (x[1], x[0]))
    accommodations = []
    unaccommodated_guests = 0
    occupied_rooms = set()

    for guest_count in args:
        best_fit = None

        for room_number, capacity in sorted_rooms:
            if capacity >= guest_count:
                best_fit = (room_number, capacity)
                break

        if best_fit:
            room_number, _ = best_fit
            accommodations.append((room_number, guest_count))
            occupied_rooms.add(room_number)
            sorted_rooms = [r for r in sorted_rooms if r[0] != room_number]
        else:
            unaccommodated_guests += guest_count

    empty_rooms = len(kwargs) - len(occupied_rooms)

    # Construct output
    if accommodations:
        result = [f"A total of {len(accommodations)} accommodations were completed!"]
        for room_number, guest_count in sorted(accommodations):
            result.append(f"<Room {room_number} accommodates {guest_count} guests>")
    else:
        result = ["No accommodations were completed!"]

    if unaccommodated_guests:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if empty_rooms:
        result.append(f"Empty rooms: {empty_rooms}")

    return "\n".join(result)

print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))