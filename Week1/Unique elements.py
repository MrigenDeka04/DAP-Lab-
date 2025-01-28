# Write a Python program that takes a list and returns a new list with unique elements of the first list.

def uniquelist(inp_list):
        out_list = []
        for i in inp_list:
                if i not in out_list:
                        out_list.append(i)
        return out_list
                
       
       
inp_list = [2, 5, 9, 3, 1, 2, 5, 0]                  
print(uniquelist(inp_list))
