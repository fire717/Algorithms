# 题目是读懂了，但是不大明白，怎么判断循环？值一样就循环吗？不然的话，不是节点总是指向next吗？难道要求物理地址？
# 查：使用快慢指针。如果链表有环，则两指针必在某一时刻相等。

if head == None:  
            return False  
          
        fast = head  
        slow = head  
          
        while fast.next != None:  
            fast = fast.next.next  
              
            if fast == None:  
                return False  
              
            slow = slow.next  
              
            if fast == slow:  
                return True  
          
        return False 
