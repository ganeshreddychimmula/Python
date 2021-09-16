#aWESOME is cODING
#swap cases in each word and reverse the cases
def reverse_order_and_swap_cases(sentence):
     list=sentence.split()              #turning given sentence into list
                            #copying into another list
     for i in range(len(list)):
         sublist=list[i].split()        #splitting each word
         for j in range(len(sublist)):
                sublist[j]=sublist[j].swapcase()
         list[i]="".join(sublist)
     list.reverse()
     temp=""
     for k in range(len(list)):
        temp=temp+" "+list[k]
     return temp.strip()

y=reverse_order_and_swap_cases(input("enter:"))
print(y)