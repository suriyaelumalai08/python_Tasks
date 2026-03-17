from Task_class import Task


my_task=Task()

methods=[method for method in dir(Task) if callable (getattr(Task,method)) and not method.startswith('__')]


for i in range(len(methods)):
    print(f'Method_no: {i+1}, Method_name: {methods[i]}\n')


try:
    n=int(input("which Method Do You want to see:"))
except Exception:
    print(Exception)


def Method_name(n):
    return f'You Select a method is:{methods[n-1]}\n'


match(n):

    case 1:
        print(Method_name(n))
        data1=input('Give a First string for Anagrams:')
        data2=input('Give a Second String for Anagrams:')
        print(my_task.Anagrams(data1,data2))
    
    case 2:
        print(Method_name(n))
        data=input('Give a string for Capitalize:')
        print(my_task.Capitalize(data))

    case 3:
        print(Method_name(n))
        data=input('Give a string for Number :')
        print(my_task.Contains_digits(data))

    case 4:
        print(Method_name(n))
        data=input('Give a string to find lenth of String:')
        print(my_task.Count_String(data))

    case 5:
        print(Method_name(n))
        data=input('Give a string to find Count frequency value:')
        print(my_task.Count_frequen(data))

    case 6:
        print(Method_name(n))
        data=input('Give a string to find the number of words:')
        print(my_task.Count_sentence(data))

    case 7:
        print(Method_name(n))
        data=input('Give a string to find the Count of Vowels:')
        print(my_task.Count_vowels(data))

    case 8:
        print(Method_name(n))
        data=input('Give a string to find the duplicate characters:')
        print(my_task.Duplicate_string(data))

    case 9:
        print(Method_name(n))
        data=input('Give a string to find the largest word:')
        print(my_task.Largest_sentence(data))

    # case 10:
    #     print(Method_name(n))
    #     data=input('Give a string to find the longest substring:')
    #     print(my_task.Longest_substring(data))

    case 11:
        print(Method_name(n))
        data=input('Give a string to find the non-repeating character:')
        print(my_task.Non_repeated(data))

    case 12:
        print(Method_name(n))
        data=input('Give a string to find the Palindrome or Not :')
        print(my_task.Palindrome(data))

    case 13:
        print(Method_name(n))
        data=input('Give a string to Remove duplicate characters:')
        print(my_task.Remove_duplicate(data))

    case 14:
        print(Method_name(n))
        data=input('Give a string to Remove spaces from a String:')
        print(my_task.Remove_spaces(data))

    case 15:
        print(Method_name(n))
        data=input('Give a string to Return a Reverse String:')
        print(my_task.Reverse(data))
    
    case 16:
        print(Method_name(n))
        data=input('Give a string for Reverse words in a sentence:')
        print(my_task.Reverse_sentence(data))

    case 17:
        print(Method_name(n))
        data=input('Give a string to Return Reverse a String without using loop:')
        print(my_task.Reverse_without_loop(data))

    case 18:
        print(Method_name(n))
        data=input('Give a string to Return Reverse a String without using Method:')
        print(my_task.Reverse_without_method(data))

    # case 19:
    #     print(Method_name(n))
    #     data=input('Give a string to Find rotation of another string:')
    #     print(my_task.Rotation_string(data))

    case 20:
        print(Method_name(n))
        data1=input('Give a first string Swap two strings:')
        data2=input('Give a second string Swap two strings:')
        print(my_task.Swap_two_string(data1,data2))
    
    case _:
        print('Invalid Input.')


