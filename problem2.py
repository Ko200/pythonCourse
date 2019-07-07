# List Comprehensions
# link https://www.hackerrank.com/challenges/list-comprehensions/submissions/code/88969855


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+