if __name__ == '__main__':
    
    result = []
    for i in range(int(input())) :
        data_input = input().split()
        data_input = [int(data) for data in data_input] # Convert to int
        result.append(min(data_input))
        
    print(" ".join([str(data) for data in result]))
    