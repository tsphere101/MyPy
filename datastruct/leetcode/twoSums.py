class Solution:
    def twosum(self,nums,target):
        def combination(L):
            if len(L) == 2:
                return [L]
            f = L[0]
            return [[f,L[x]] for x in range(1,len(L))] + combination(L[1:])

        def sum_list(L):
            result = 0
            for data in L:
                result += data 
            return result
        
        result = list()
        comb = combination(nums)
        for each_pair in comb:
            if sum_list(each_pair) == target:
                result += each_pair
                break
        result_index =  list()       
        for d in result:
            ind = nums.index(d)
            if ind in result_index:
                nums.pop(ind) 
                ind = nums.index(d) + 1
            result_index.append(ind)
        return result_index

if __name__ == "__main__":
    a = Solution()
    input_list = [map(int,input("Enter : ").split(","))]
    print(a.twosum(input_list,int(input())))