"""
leetcode 841
"""

def canVisitAllRooms(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    l = len(rooms)
    room_was_entered = [False] * l
    entered_rooms = 0
    key_ring = [0]
    while len(key_ring):
      key = key_ring.pop()
      if not room_was_entered[key]:
        room_was_entered[key] = True
        entered_rooms += 1 
        for key_found in rooms[key]:
          key_ring.append(key_found)
        
    return entered_rooms == l 
