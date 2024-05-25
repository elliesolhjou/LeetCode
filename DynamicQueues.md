***Static Queue Limitations ***   
• Capacity are fixed    
• Allocating too much memory is wasteful    
• Allocating too little memory makes array too limited 
 
***What are Dynamic Queues?***  
• Queues without a fixed capacity
• Usually implemented using a dynamic structure, such as a dynamic array
• Check capacity after any operation that modifies the count of elements


***Dynamic Queue Algorithm***   
1. When calling enqueue, if count >= capacity:  
    • Allocate double the capacity of current array      
    • Copy contents of current array to new array           
    • Starting from front until count           
2. Point to the new array
3. Set front to 0
