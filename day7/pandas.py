import numpy as np
def p1():
    values = np.linspace(0, 100, 5)
    print("Generated values:", values)
    print("Total count:", len(values))
def p2():
    import numpy as np
    array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])
    mean   = np.mean(array)
    median = np.median(array)
    print(f'Mean = ', mean)
    print(f'Median = ', median)
def p3():
    array1 = np.array([[1, 2], [3, 4]]) 
    array2 = np.array([[1, 2], [3, 4]]) 

    print(array1 == array2) # Does element wise comparison and returns truth value for every comparison which is again stored in the respective sized np array

    comparison = (array1 == array2)
    equal_arrays = comparison.all() # Here all the truth values of the inferred np array is taken and if all are True then it returns True, else False.

    print(equal_arrays)
def p23():
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import pandas as pd
    from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

    x = np.linspace(0, 10, 100)  # Generating 100 points between 0 and 10
    y = np.sin(x)  # Sine function

    plt.plot(x, y, label="Sine Wave")  # Plot sine wave
    plt.xlabel("X-axis")  # Label for x-axis
    plt.ylabel("Y-axis")  # Label for y-axis
    plt.title("Line Plot")  # Title of the plot
    plt.legend()  # Display legend
    plt.show()  # Show the plot
def p4():
    import numpy as np
    week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
    highest_spending = max(week_spendings)
    print(highest_spending)
def p5():
    import numpy as np
    week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
    index = 1
    index = np.argmax(week_spendings)
    days = {1:'mon', 2:'tue', 3:'wed', 4:'thus', 5:'fri', 6:'sat', 7:'sun'}
    print(days[index+1])
def p6():
    expenses = np.array([20, 60, 5, 80, 45, 90])
    modified_expenses = np.where(expenses < 50, 0, expenses)
    print(modified_expenses)
def p7():
    random_data = np.random.rand(3, 4) # Creates a 3x4 array with random values
    print(random_data)
def p8():
    import math
    import random
    user_number = int(input('Enter a number of your choice between [0 and 9]: '))
    system_number = random.randint(0,9)
    if system_number == user_number:
        print('CrorePati')
    else:
        print('RoadPati')
def p9():
    sequence_arange = np.arange(0,100,5)  # Generates values from 1 to 10 with a step of 3
    sequence_linspace = np.linspace(0, 100, 5)  # Generates 5 equally spaced values between 0 and 100
    print("Using arange:", sequence_arange)
    print("Using linspace:", sequence_linspace)
def p10():
    
    import pandas as pd
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'Salary': [50000, 60000, 70000]}
    df = pd.DataFrame(data)
    print(df)

def p25():
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import pandas as pd
    from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

    categories = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 25]

    plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Bar Chart")
    plt.show()
def p26():
    import numpy as np

    my_array = np.zeros((4, 4), dtype = int)
    my_array[1::2, ::2] = 1
    #Starting from row-index-1 and there after, for all alternatives rows, and for all columns from index 0 and there after alternative columns, replace the cells with value 8
    my_array[::2, 1::2] = 1
    # Odd indexed-rows Even Indexed-Columns
    print(my_array)                                     
def p27():
    list1 = [2, 3, 5]

    string = ' '.join(map(str, list1)) # convert a list of items of tyep other than str into a string
    print(string)
    print(type(string))

    list2 = ['23', '55', '67']
    string = ' '.join(list2) 
    print(string)
def p28():
        
    chess_board = np.tile( np.array([[1, 0],[0, 1]]), (4,4))
    # chess_board = np.tile( np.array([['*', ' '],[' ', '*']]), (4,4))
    #print('\n', chess_board)

    list1 = []
    for array in chess_board:
        list1 = list(array)
        string = ' '.join(map(str, list1))
        print(string)   
def p29():
    import numpy as np

    my_array = np.random.random((5,5))
    #print(my_array)

    values = my_array - np.mean (my_array)
    print('\n', values)

    values = np.std (my_array)
    print('\n', values)

    my_array = (my_array - np.mean (my_array)) / (np.std (my_array))
    print(my_array)

def p30():

    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import pandas as pd
    from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

    categories = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 25]

    plt.barh(categories, values, color='orange')
    plt.xlabel("Values")
    plt.ylabel("Categories")
    plt.title("Horizontal Bar Chart")
    plt.show()
def p31():
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import pandas as pd
    from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

    data = np.random.randn(1000)

    plt.hist(data, bins=30, color='green', edgecolor='black')
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

def p32():
    import matplotlib.pyplot as plt
    import numpy as np

    # Generate 100 points between 0 and 10
    x = np.linspace(0, 10, 100)  
    # Compute sine function values
    y = np.sin(x)  

    # Plot sine wave
    plt.plot(x, y, label="Sine Wave")  
    plt.xlabel("X-axis")  # Label for x-axis
    plt.ylabel("Y-axis")  # Label for y-axis
    plt.title("Line Plot")  # Title of the plot
    plt.legend()  # Display legend
    plt.show()  # Show the plot

def p33():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.random.rand(50)
    y = np.random.rand(50)

    # Create scatter plot
    plt.scatter(x, y, color='red', marker='o')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot")
    plt.show()  
p33()