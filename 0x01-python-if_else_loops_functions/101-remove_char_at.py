#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str):
        st=""
        for i in range(0, n):
            st=st+str[i]
        for i in range(n+1,len(str)):
            st=st+str[i]
    return (st)
        
