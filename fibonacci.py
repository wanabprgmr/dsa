# import psutil 
# import os

# process = psutil.Process(os.getpid())
 
# # Get CPU usage 
# cpu_usage = psutil.cpu_percent() 
 
# # Get memory usage 
# memory_usage = psutil.virtual_memory().percent 

# base_memory_usage = process.memory_info().rss
 
# print(f"CPU Usage: {cpu_usage}%") 
# print(f"Memory Usage: {memory_usage}%") 
# prev2 = 0
# prev1 = 1

# for fibo in range(100):
#     newfibo = prev2 + prev1
#     print(newfibo)
#     prev2 = prev1
#     prev1 = newfibo
#     memory_usage = process.memory_info().rss
#     loop_memory_usage = memory_usage - base_memory_usage
#     # print("memory status:", base_memory_usage)
#     # print("memory status:", memory_usage)
#     print("memory status:", loop_memory_usage)
    
#  recurssion method

# print("0")
# print("1")
# count = 1

# def fib(num1, num2):
#     global count
#     while count < 10:
#         newfib = num1 + num2
#         print(newfib)
#         count += 1
#         fib(num2, newfib)
        
# fib(0, 1)
    
    
# find nth fibonacci number

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)


print(F(5))
