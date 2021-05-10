import argparse

def get_args():
    parser = argparse.ArgumentParser(description='List Practice',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    return args

def sampleFunction(argument1):
    print ("hello" + argument1)

def main():
    args = get_args()
    #1
    print('Exercise 1')
    my_list11 = []
    my_list12 = [1,2,3]
    my_list13 = [1,'hello',3,4]
    my_list14 = ['hello',[1,2,4],['X']]
    
    #2
    print('Exercise 2')
    my_list21 = ['H','E','L','L','O']
    print(my_list21[0])
    n_list22 = ["Hello",[1,2,3,4]]
    print(n_list22[0][1])
    print(n_list22[1][3])

    #3
    print('Exercise 3')
    my_list31 = ['H','E','L','L','O']
    print(my_list31[-1])

    #4
    print('Exercise 4')
    my_list41 = ['H','E','L','L','O','w','o','r','l','d']
    print(my_list41[2:5])
    print(my_list41[:-6])
    print(my_list41[5:])
    print(my_list41[:])

    #5
    print("Exercise 5")
    odd5 = [2, 4, 6, 8]
    odd5[0] = 1
    print(odd5)
    odd5[1:4] = [3, 5, 7] # --> [1,3,5,7]
    #odd5[1:3] = [3, 5, 7] # --> [1,3,5,7,8]
    print(odd5)


    #6
    print("Exercise 6")
    odd6 = [1,3,5]
    odd6.append(7)
    print(odd6)
    odd6.extend([9,11,13])
    print(odd6)

    #7
    print("Exercise 7")
    odd7 = [1,3,5]
    print(odd7 + [7,9,11])
    print(['re']*7)

    #8
    print("Exercise 8")
    odd8 = [1,9]
    odd8.insert(1,3)
    print(odd8)
    odd8[2:2]=[5,7]
    print(odd8)

    #9
    print("Exercise 9")
    my_list9 = ['H','E','L','L','O']
    del my_list9[2]
    print(my_list9)
    del my_list9[1:5]
    print(my_list9)

    #10
    print("Exercise 10")
    my_list10 = ['p','r','o','b','l','e','m']
    my_list10.remove('p')
    print(my_list10)
    print(my_list10.pop(0)) #--> 'r'
    print(my_list10) #--> ['o', 'b', 'l', 'e', 'm']
    my_list10.clear()
    print(my_list10)

    #11
    print("Exercise 11")
    my_list11 = ['p','r','o','b','l','e','m']
    my_list11[2:3] = []
    print(my_list11)

    #12
    print("Exercise 12")
    my_list12 = [3, 8, 1, 6, 0, 8, 4]
    print(my_list12.index(8)) # --> 1
    print(my_list12.count(8)) # --> 2
    my_list12.sort()
    print(my_list12) # ->[0, 1, 3, 4, 6, 8, 8]
    my_list12.reverse()
    print(my_list12) # ->[8, 8, 6, 4, 3, 1, 0]

    #13 LIST COMPREHENSION
    print("Exercise 13 - List Comprehension")
    pow2 = [2 ** x for x in range(10)]
    print(pow2) #--> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    pow2 = []
    for x in range(10):
        pow2.append(2 ** x)
    
    #14
    print("Exercise 14")
    #pow2 = [2 ** x for x in range(10) if x > 5]
    pow2 = [2**x for x in range(10) if x > 5]
    print(pow2) #--> [64, 128, 256, 512]
    odd = [x for x in range(20) if x % 2 == 1] #--> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(odd)
    [x+y for x in ['Python ','C '] for y in ['Language','Programming']] #--> ['Python Language', 'Python Programming', 'C Language', 'C Programming']

    #15
    print("Exercise 15")
    my_list15 = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    print('p' in my_list15) #-->T
    for fruit in ['apple','banana','mango']:
        print("I like",fruit)

    print("Exercise 16")
    h_letters = [ letter for letter in 'human' ]
    print( h_letters)

    #lambda
    print("Exercise-lambda")
    sampleFunction("Felipe")
    letters = list(map(lambda x: x, 'human'))
    print(letters)

    #17
    print("Exercise 17")
    number_list = [ x for x in range(20) if x % 2 == 0]
    print(number_list)

    #18
    print("Exercise 18")
    num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
    print(num_list)

    #if..else
    print("Exercise if..else")
    obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
    print(obj)

    #19
    print("Exercise 19")
    transposed = []
    matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)
    print()

    matrix2 = [[1, 2], [3,4], [5,6], [7,8]]
    l = [[row[i] for row in matrix2] for i in range(2)]
    print(l)

if __name__ == '__main__':
    main()