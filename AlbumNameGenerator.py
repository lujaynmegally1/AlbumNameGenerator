import random 

class album_name_generator:
    """
    A class for generating a random album name when user enters a genre and word length. 
    Count the number of occurrences of each character in a string. 
    s: str, the string in which to count. 
    return counts, a dict keyed by character whose values are the number of  occurrences in s
    """ 
    def __init__(self):
        """
        Count the number of occurrences of each character in a string. 
        s: str, the string in which to count. 
        return counts, a dict keyed by character whose values are the number of  occurrences in s
        """
        # checks if string_length is an int
        while True:
            try:
                string_length = int(input("How many words do you want your album name to be? \n"))
                break
            except ValueError:
                print("Not a valid number.  Try again...")

        # checks if genre is a valid choice 
            
        while True: 
            try: 
                genre = input("What genre do you want your album to be? Choices: Rap, Pop, Rock \n")
                if genre == "Rap" or genre == "Pop" or genre == "Rock": 
                    break 
                else: 
                    raise NameError ()
            except NameError:
                print ("Choice not valid. Try again...") 
                
        self.genre = genre 
        self.string_length = string_length

        words = random.sample(self.file_list(self.genre_file()), self.string_length)
        self.album_name = " ".join(words)
        
        print(self.album_name)
        
        
    def genre_file(self):
        # opens the file with inputted genre name 
        filename = "%s.txt" % self.genre.lower()
        with open(str(filename), 'r') as f:
            s = f.read()
        return s 

    def file_list(self, s):
        '''
        Takes in the text file of the chosen genre, which contains newline characters and no spaces,
        and splits it so that the result is a list of the 50 words from that file
        Args: s, a text file containing words specific to the user's chosen genre
        Returns: s, the words in the original text file converted into a list of 50 strings
        '''
        # replaces \n with a space in string s
        s = s.replace("\n", " ")
        # turns s into a list of words 
        s = s.split()
        return s 
        
    def __str__(self):
        #generates a random set of words from list s, with length string_length
        album_name = self.album_name
        return album_name
    

    
        
   
