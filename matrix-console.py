from random import randint


min_item_number = 7
max_item_number = 10



def generate_item_number():
        # ham nay de tao ra arr random cac so [7,8,9]
        a = []
        for i in range(3):
                a.append(randint(min_item_number,max_item_number))
        return a


def generate_list_item():
        # tao ra mot array table gom 27 slot for 27 item random
        a = [0] * 3
        b = [a] * 27
        return b


def change_table_to_1_array(table):
        table_0=[]
        table_1=[]
        table_2=[]
        for i in range(27):
                if i / 9 == 0:
                        table_0.append(table[i])
                if i / 9 == 1:
                        table_1.append(table[i])
                if i / 9 == 2:
                        table_2.append(table[i])
        
        new_table_0 = [0] * 27
        new_table_1 = [0] * 27
        new_table_2 = [0] * 27
        for j in range(9):
                for i in range(3):
                        new_table_0[9*i + j] = table_0[j][i]

        for j in range(9):
                for i in range(3):
                        new_table_1[9*i + j] = table_1[j][i]

        for j in range(9):
                for i in range(3):
                        new_table_2[9*i + j] = table_2[j][i]

        return new_table_0+new_table_1+new_table_2


def print_table(new_table):
        for i in range (9):
                a = ''
                for j in range(9):
                        if new_table[j+i*9] > 9:
                                a = a + ' ' + str(new_table[j+i*9])
                        else:
                                a = a + '  ' + str(new_table[j+i*9])                                
                print a
        print("")


def calcu_score_row(arr):
        max_index = len(arr)

        sum = 0
        a = arr[0]

        count_same = 0
        for b in range(1,max_index,1):
                if arr[b] == a:
                        count_same = count_same + 1
                if arr[b] != a:
                        
                
                print sum   
        print sum

calcu_score_row([8,7,7,7,8])            
                
#  7 7 7 8 
#  x x x 0

def calcu_score(new_table):
        for i in range():
                pass
        
        

# table = generate_list_item()
# for i in range(27):
#         new_item = generate_item_number()
#         print(new_item)
#         table[i] = new_item
# new_table = change_table_to_1_array(table)
# print_table (new_table)


