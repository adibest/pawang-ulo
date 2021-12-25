def factorialUsingRecursion(n):
    if (n == 0):
        return 1;
 
    # recursion call
    return n * factorialUsingRecursion(n - 1);

n = int(input("Masukkan data:"))
print("Hasil factorial bilangan ",n, "adalah:",factorialUsingRecursion(n))