from SearchEngine import *
import time
if __name__ == "__main__":
    se = SearchEngine("zen_record.txt")
    sp = SpellCorrection(dictionary_path="dictionary.txt")

    kw = input()
    t0 = time.time()
    x = se.search_by_keyword(keyword=kw, return_value ='Quote',number_of_result = 20)
    t1 = time.time()
    if x:
        for i,data in enumerate(x):
            print(i+1,data.replace(kw,"'"+kw+"'"))
    else :
        print('DOES NOT MATH ANY WORDS.')
    
    print(t1-t0)
