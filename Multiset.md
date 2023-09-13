Create a python 3 code  
multiset is the same as a set expect than an element might occur more than once inpython. given a templete for the multiset class implement 4 methods:- 
1. Add(self, val): adds val to the multiset 
2. remove(self, val): if val is in the multiset, removes val from the multiset: otherwise do nothing 
3. _contains_(self,val): return true if val is in the multiset; otherwise it return False
4. _len_(self, val): returns the number of element in the multiset

additional methods are allowed as neccessary 
the implementaion of the 4 required methods will be tested by a provided code stub on sevral input files each input file contains several operations each of one of the below types values returened by query and size operation are appended to a result list which is printed as the output by the provided code stub .

1. add val: calls add(val) on the multiset instance
2.remove val; calls remove(val) on the multiset instance
3.query val: appends the results of expression val in m, where m is an instance of multiset, and appends the value of that expresssion on the result list
4. size : calls len(m), where m is an instance of multiset and appends the return value to the result list

comlete the class multiset in the editior below with 4 methods given above (add, remove,_contains_,_len_,and _len_)

constraints:
1. 1<= number of the operation in one test file <+ 10 power to 5
2.if val is a parameter of operation then val is an integer and 1<= val <= 10 to power 9

Explanation

There are 12 operations to be performed. Start with an empty

multiset: multiset = []. 1. The first operation asks if 1 is in the multiset. It is not, so False is

appended to the result: result = [False]. 2. The second operation adds 1 to the multiset: multiset = [1].

3. The third operation asks if 1 is in the multiset. It is now, so True Is appended to the result: result = [False, True].

4. The fourth operation removes 1 from the multiset: multiset = []). 5. The fifth operation asks if 1 is in the multiset. It is not, so False is

appended to the result: result = [False, True, False). 6. The sixth operation adds 2 to the multiset: multiset = [2].

7. The seventh operation adds 2 to the multiset: multiset = [2,2]. 8. The next operation asks what is the size of the multiset: result =

[False, True, False, 2]. 9. The next operation asks if 2 is in the multiset. It is, so True is

appended to the result: result = [False, True, False, 2, True].

10. The next operation removes 2 from the multiset: multiset = [2] 11. The next operation asks if 2 is in the multiset. It is, so True is appended to the result: result = [False, True, False, 2. True, True).

12. Finally, the last operation asks for the size of the multiset and the length, 1, is appended to the result. result = [False, True, False, 2, True, True, 1]


This is input:- 

12
query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size

expected output: 

False
True
False
2
True
True
1
