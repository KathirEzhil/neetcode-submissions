class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def uniquecheck(collection):
            nums = ["1","2","3","4","5","6","7","8","9","."]
            unique = []
            for i in collection:
                if i not in nums:
                    return False
                if i in unique and i != ".":
                    return False
                else:
                    unique.append(i)
            return True

        flag = True 

        for row in board:
            flag = uniquecheck(row)
            print(row)
            print()
            if flag == False:
                return False
        
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            flag = uniquecheck(col)
            print("============")
            print(col)
            print()
            if flag == False:
                return False
        
        # separate into small squares

        arrays = []

        top = board[:3]
        t1,t2,t3 = [],[],[]
        for array in top:
            l1 = array[:3]
            t1.extend(l1)
            l2 = array[3:6]
            t2.extend(l2)
            l3 = array[6:9]
            t3.extend(l3)
        arrays.append(t1)
        arrays.append(t2)
        arrays.append(t3)
            
        middle = board[3:6]
        t1,t2,t3 = [],[],[]
        for array in middle:
            l1 = array[:3]
            t1.extend(l1)
            l2 = array[3:6]
            t2.extend(l2)
            l3 = array[6:9]
            t3.extend(l3)
        arrays.append(t1)
        arrays.append(t2)
        arrays.append(t3)

        bottom = board[6:9]
        t1,t2,t3 = [],[],[]
        for array in bottom:
            l1 = array[:3]
            t1.extend(l1)
            l2 = array[3:6]
            t2.extend(l2)
            l3 = array[6:9]
            t3.extend(l3)
        arrays.append(t1)
        arrays.append(t2)
        arrays.append(t3)

        print("============")
        print(arrays)
        print()

        for array in arrays:
            flag = uniquecheck(array)
            if flag == False:
                return False
        return True

        


            
            
        