def findOrder(numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
  def dfs(course):
    # if its currently being visited (indicates a cycle)
    if visiting[course]:
      return False

    # if its already been processed, no need to check again
    if course in processed:
      return True

    # mark as being visited currently
    visiting[course] = 1

    for prereq in graph[course]:
      if not dfs(prereq):
        return False

    # finished visiting all the prereqs and didn't hit a cycle
    visiting[course] = 0 
    processed.add(course)
    course_order.append(course)

    return True
  
  

  course_order = [] 
  graph = [[] for _ in range(numCourses)]
  visiting = [0] * numCourses
  processed = set()

  for course, prereq in prerequisites:
    graph[course].append(prereq)

  for i in range(numCourses):
    if not dfs(i):
      return []

  return course_order 
