'''
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
 
'''

class Solution:

    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # sandwich=[0,0,0,1,1,0,1,0]
        # student=[0,0,1,1,1,0,1,0]
        # queue -> FIFO -> Dequeue/Enqueue ->LinkedList
        # sandwichCount -> Stacked
        # len student = count
        # first in -> take it from top of stack or leave it
        # if take from top of stack-> dequeue
        # if leave and no stack touch -> dequeue and enqueue
        # till student [i] ! = sandwich[j]

        #  TOP OF STACK MEANS FIRST ELEMENT OF STACK
        while students and sandwiches:
            print(f"studnet original:{students} and sandwich stack original: {sandwiches}")
            if students[0] != sandwiches[0]:
                hungry = students.pop(0)
                students.append(hungry)
                print("new enque/deque student queue", students, "and student queue length is", len(students))
                    
            else:
                print (f"student wants {students[0]} type and the sandwich at top of stack is type {sandwiches[0]}")
                students.pop(0)
                print(f"new student queue, {students}, and we have, {len(students)} students left")
                sandwiches.pop(0)
                print("new sandwich stack", sandwiches, f"with {len(sandwiches)} sandwiches left")

            # to make sure none of students preferences matches sandwich on top so no reque/deque would require -> 
                # students=[1,1]
                # sandwiches=[0,1]
            if all(student != sandwiches[0] for student in students):
                break
            
        
        print(f"conditions are not met anymore and here is list of students left {students} and here is sandwiches{sandwiches}")
        
        print (f"{len(students)} students are hungry")
        return f"{len(students)} students are hungry"

sol = Solution()
result = sol.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])



