<h1>Data Structures and Algorithms in Python</h1>
Repository that shows most algorithms and patterns that would be useful in solving dsa problems, especially for someone like me that doesn't really use python for dev work but rather use it since implementations of solution are easier in python due to the availability of libraries that abstract the complexity of implementation of certain data structures

## Stack ADT
This largely uses the ```collections module```
<br />
Interested submodules are ```deque```

## Hash Table ADT
This largely uses the ```collections module```
<br />
Interested submodules are ```defaultdict``` and ```ordereddict```

## Priority Queue ADT

### Heap Data Structure Implementation
This largely uses the ```heapq module```
Documenation can be referenced from: [here](https://docs.python.org/3/library/heapq.html#).
<br />

```
Note: heapq module would implement a min heap by default!
Easy Solution whilst retaining the same functions would be to multiply the elements of the heap by -1 !
```

**Heapify Operation**
<br />
Time Complexity: O(N)
```python
import heapq as hq

list_stu = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'cathy'),(4,'Lucy')] 
hq.heapify(list_stu) 

```
It is noted that we would have to include tuples with the **first** element of the tuple representing the **priority**.

**Heap Insert**
Time Complexity: O(logN)
```python
hq.heappush(heap, newTuple) 
```

**Heap Removal**
Time Complexity: O(logN)
```python
hq.heappop() 
```
