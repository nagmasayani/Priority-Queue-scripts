#!/usr/bin/env python
# coding: utf-8

# In[5]:


import queue

# Step 1: Create a Priority Queue
School_List = queue.PriorityQueue()

# Step 2: Add elements to the Priority Queue
School_List.put((2, "Pens"))
School_List.put((1, "Pencil"))
School_List.put((3, "Eraser"))

# Step 3: Pop an element from the Priority Queue
popped_element = School_List.get()

# Step 4: Show the output
print("Popped element:", popped_element)

remaining_elements = []

while not School_List.empty():
    remaining_elements.append(School_List.get())

print("Remaining elements in the queue:")
for element in remaining_elements:
    print(element)


# In[ ]:




