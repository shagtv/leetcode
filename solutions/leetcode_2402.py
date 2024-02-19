from heapq import heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda k:k[0])

        rooms = [(0, room_id) for room_id in range(n)]
        used_rooms = [0] * n
        for start, end in meetings:
            unused_rooms = {}
            min_room_id = None
            while rooms:
                time, room_id = heappop(rooms)
                unused_rooms[room_id] = time
                if time <= start:
                    if  min_room_id == None or room_id < min_room_id:
                        min_room_id = room_id
                else:
                    if  min_room_id == None:
                        min_room_id = room_id
                    break
            duration = end - start
            used_rooms[min_room_id] += 1
            unused_rooms[min_room_id] = max(start, unused_rooms[min_room_id]) + duration
            for room_id in unused_rooms:
                heappush(rooms, (unused_rooms[room_id], room_id))
        min_room_id = 0
        min_room_count = 0
        for room_id, count in enumerate(used_rooms):
            if count > min_room_count:
                min_room_count = count
                min_room_id = room_id
        return min_room_id


if __name__ == '__main__':
    given_n = 2
    given_meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
    expected = 0

    solution = Solution()
    result = solution.mostBooked(given_n, given_meetings)
    assert result == expected
