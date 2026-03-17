class Task:

    # Reverse a String.

    def Reverse(self,data: str) -> str:
        """
        This is Method for to Reverse a String Useing the Python slicing method
        """
        return data[::-1]
    
    
    # Check whether a String is Palindrome.

    def Palindrome(self,data: str) ->str:
      """Check whether the given string is a palindrome."""

      if data ==data[::-1]:
         return "palindrome"
      else:
         return "Not palindrome"


      #Count number of characters in a String.

    def Count_String(self,data: str) ->str:
       """Return the total number of characters in the given string.
        And Not Using the len() function."""
       
       count=0
       for i in data:
          count+=1

       return count
    
    
    # Count vowels and consonants in a String.

    def Count_vowels(self,data: str)->str:
        """Count the number of vowels and consonants in the given string."""

        Vowels=0
        Consonants=0

        for i in data:
           if i.lower() in "aeiou":
              Vowels+=1
           else:
              Consonants+=1
        
        return f"Vowels:{Vowels},Consonants:{Consonants}"
    
    
    # Remove spaces from a String.

    def Remove_spaces(self,data: str) ->str:
       """Remove all spaces from the given string.
       Using the Replace Per-Define Function.
       """
       return data.replace(' ','')
    
    
    # Count number of words in a sentence
    
    def Count_sentence(self,data: str) ->str:
       """Return the number of words in the given sentence.
       Using Split() Function
       """
       count=0

       data=data.split()

       for _ in data:
          count+=1
        
       return count
    
    
    #  Find duplicate characters in a String

    def Duplicate_string(self,data: str) ->str:
       """Identify duplicate characters in the given string."""

       find=set()

       result=[]

       for i in data:
          if i not in find:
             find.add(i)
          else:
             result.append(i)

       return tuple(result)
    
    
    # Find the first non-repeating character.

    def Non_repeated(self,data: str) ->str:
       """Return the first non-repeating character in the given string."""

       result=[]
       
       for i in data:
          if i not in result:
             result.append(i)
          else:
             result.remove(i)
       
       return result[0]
    
    
    # Check whether two strings are anagrams.
    
    def Anagrams(self,data1: str, data2: str) ->str:

        """Check whether the two given strings are anagrams."""

        if sorted(data1) == sorted(data2):
           return 'Anagrams'
        else:
           return 'Non-Anagrams'
        
        
    # Count frequency of each character in a String

    def Count_frequen(self,data: str) ->str:
       """Count the frequency of each character in the given string."""

       result={}

       for i in data:
          if i in result:
            result[i]=result[i]+1

          else:  
             result[i]=1
      
       return result
    
      #Reverse words in a sentence
      
    def Reverse_sentence(self,data: str) ->str:
       """Reverse the order of words in the given sentence."""
       data=data.split()
       n=len(data)//2
       left=0
       right=len(data)-1
       result=''

       for i in range(n):
          data[left],data[right]=data[right],data[left]
          left+=1
          right-=1
       
       for i in data:
          result += i +' ' 

       return result.strip()  
    
    # Remove duplicate characters from a String.

    def Remove_duplicate(self,data: str) ->str:
       """Remove duplicate characters from the given string."""
       result=''
       for i in data:
         if i not in result:
            result+=i
       
       return result
    
    # Find the largest word in a sentence.

    def Largest_sentence(self,data: str) ->str:
       """Return the longest word in the given sentence."""

       data=data.split()
       
       result1=0

       for i in range(len(data)):
         if result1<len(data[i]):
            result1=len(data[i])
            result2=""
            result2+=data[i]

       return result2
    
     # Capitalize first letter of every word

    def Capitalize(self,data: str) ->str:
       """Capitalize the first letter of each word in the given string."""
       
       return data.capitalize()
    
    # Check if a String contains only digits.

    def Contains_digits(self,data: str) ->str:
       """Check whether the given string contains only digits."""

       return data.isnumeric()
    
   # Reverse a String without using reverse() method.

    def Reverse_without_method(self,data: str) ->str:
       """Return the reversed string without using built-in reverse methods."""
       n=len(data)
       result=''

       for i in range(n,0,-1):
          result+=data[i-1]

       return result
    
    # Reverse a String without using loop

    def Reverse_without_loop(self,data: str) ->str:
       """Return the reversed string without using loops."""

       return data[::-1]
   
   # Swap two strings without using third variable.

    def Swap_two_string(self,data1: str, data2: str) ->str:
     """Swap the values of two strings without using a third variable."""

     data1,data2=data2,data1

     return f'{data1},{data2}'
    
    
   # Find longest substring without repeating characters.

    def Longest_substring(self,data: str) ->str:
       """Return the longest substring without repeating characters."""
       pass
    
    
    # Check whether a String is rotation of another string

    def Rotation_string(self,data1: str, data2: str) ->str:
       """Check whether one string is a rotation of another string."""
       pass

       


    





    

       
             
          






    

        
          
    
      
        


    

    
