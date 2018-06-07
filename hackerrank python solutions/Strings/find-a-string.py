def count_substring(string, sub_string):
    c=0
    for i in range(0,len(string)-len(sub_string)+1):
        if(sub_string==string[i:i+len(sub_string):1]):
            c=c+1;
    return(c)