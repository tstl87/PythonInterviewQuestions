class Solution:
  def canFinish(self, numCourses, prereqs):

    # graph will contain classes as keys with a list of prerequisites as values
    graph = {}
    for prereq in prereqs:
      if prereq[0] not in graph:
        graph[prereq[0]] = [prereq[1]]
      else:
        graph[prereq[0]].append(prereq[1])

    # check each course for a cycle
    for course in range(numCourses):
      if self._hasCycle(course, graph, set(), {}):
        return False

    return True

  def _hasCycle(self, course, graph, seen, cache):
    # -course: is an integer
    # -graph: is a dictionary with course integers as keys and lists of integer courses as prereqs
    # -seen: is a set of courses seen so far
    # -cache: is a dictionary with course integers as keys and boolean values to keep track of which
    # courses we've already checked for cycles so we don't check again.

    # if course is not in graph, then it has no prerequisites and can't have a cycle
    if course in cache:
      return cache[course]
   
    if course in seen:
      return True
    if course not in graph:
      return False

    # add course currently being looked at to seen.
    seen.add(course)
    # set return value to false
    ret = False
    for neighbors in graph[course]:
      if self._hasCycle( neighbors, graph, seen, cache):
        # course has been see. Set the return value to true 
        ret = True
    
    # course does not have a cycle. Remove it from seen
    # to remove any future conflict.
    seen.remove(course)

    cache[course] = ret
    return ret
  
print(Solution().canFinish(2, [[1, 0]]))
# True

print(Solution().canFinish(2, [[1, 0], [0, 1]]))
# False