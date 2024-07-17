'''INSERT FUNCTION
    PARAMETERS: TERNARY TREE
                 WORD TO BE INSERTED
    DEFINITION: A RECURSIVE APPROACH TO INSERTING A WORD INTO THE TERNARY TREE'''
def insert(tree:dict, word:str):
    if not word:       #base case
        return

    char = word[0]   #assigning the first letter of the word 
    
    if 'root' not in tree:
        tree['root']=char   #making the root of the tree as the first letter of the word
        if len(word)==1:
            tree['end_of_word']=1   #assigning a flag value of the end of word as 1/meaning word is finished 
            tree['mid'],tree['right'],tree['left']={},{},{}  #assigning the rest(mid, left, right) as empty dictionaries
            return
        else:
            tree['end_of_word'] = 0
            tree['mid'],tree['right'],tree['left']={},{},{}  #if the subtrees are all empty and end of word is 0, then the word will get inserted
            insert(tree['mid'],word[1:])
        

    elif tree['root']==None:   #for the first word only 
        tree['root']=char
        insert(tree['mid'],word[1:])  #inserting the word in the middle
        
    
    #how the letters are getting inserted into the tree
    else:
        if char<tree['root']:
            insert(tree['left'],word)   #value is lesser then its gonna get added onto the left subtree
        elif char>tree['root']:
            insert(tree['right'],word)   #value is greater then it will get added into the right sub tree 
        
        else:
        
            if len(word)==1:  #if the length of the word is 1, then the end of word is assigned as 1
                tree['end_of_word']=1
            else:
                insert(tree['mid'],word[1:])   #else add the rest of the word at the middle subtree

'''TRAVERSE FUNCTION
    PARAMETERS: TERNARY TREE
                
    DEFINITION: A RECURSIVE APPROACH TO OUTPUT ALL THE WORDS IN THE TERNARY TREE'''
def traverse(tree:dict, result:list, prefix=''):
    if 'root' not in tree:   #base case
        return

    if tree['end_of_word'] == 1:
        result.append(prefix + tree['root'])  #adding the prefix with the root if that word's end of word value is 1

    traverse(tree['left'], result, prefix)     #following the inorder traversal as in binary search in this case as in left, mid and then right
    traverse(tree['mid'], result, prefix + tree['root'])
    traverse(tree['right'], result, prefix)


'''EXIST FUNCTION
    PARAMETERS: TERNARY TREE
                WORD TO CHECK THE EXISTENCE 
                
    DEFINITION: A RECURSIVE APPROACH TO CHECK THE EXISTENCE OF A WORD IN THE TERNARY TREE'''
def exist(tree: dict, word: str) -> bool:
    #can also be named as the searching function
    if not word:  #base case
        return False

    char = word[0]

    if 'root' not in tree:
        return False      #returning boolean values 

    if tree['root'] == char:
        if len(word) == 1:
            return tree.get('end_of_word', 0) == 1  #if word is finished 
        return exist(tree.get('mid', {}), word[1:])  #return the word 
    elif char < tree['root']:
        return exist(tree.get('left', {}), word)  #check the left and right sub trees for the words which match all the letters in the word to search
    else:
        return exist(tree.get('right', {}), word)


'''DELETE FUNCTION
    PARAMETERS: TERNARY TREE
                WORD TO BE DELETED
    DEFINITION: A RECURSIVE APPROACH TO DELETE THE WORD FROM THE TERNARY TREE'''
def delete(tree: dict, word: str):
    if not exist(tree, word):
        print("The word '{}' does not exist in the tree.".format(word))  #returning this statement
        return

    delete_helper(tree, word, 0)  #calling the delete helper function in the  delete function


def delete_helper(tree: dict, word: str, index: int):
    if not tree:   #base case
        return

    char = word[index]
    if char == tree['root']:
        if index == len(word) - 1:
            if tree.get('end_of_word', 0) == 1: #checking if the end of word is 1, then make it 0
                del tree['end_of_word']
                
                if not tree.get('left') and not tree.get('mid') and not tree.get('right'):
                    del tree['root']  #delete the root from the tree to delete the word
            return
        delete_helper(tree.get('mid', {}), word, index + 1)
        
        
        if not tree.get('mid') and not tree.get('left') and not tree.get('right'):
            del tree['root']   #checking if the word is not more on either trees so then delete it
    elif char < tree['root']:
        delete_helper(tree.get('left', {}), word, index)   #checking which side the word is continued by comparing the letters of the word to delete/left side
    else:
        delete_helper(tree.get('right', {}), word, index)  #inputted at the rigth hand side



'''RETURN TREE FROM A NODE FUNCTION
    PARAMETERS: TERNARY TREE
                WORD AFTER WHICH THE SUBTREE IS NEEDED
    DEFINITION: A RECURSIVE APPROACH TO OUTPUT THE SUBTREE AFTER A WORD HAS BEEN FOUND'''
def return_tree(tree,word):
    if not word:     #base case
        return False

    char = word[0]   #assigning the first letter of the word as char

    if 'root' not in tree:
        return False           #booolean value if root not in tree

    if tree['root'] == char:
        if len(word) == 1:
            return tree['mid']   
        return return_tree(tree.get('mid', {}), word[1:])  #returning the word in the middle/if the root of te tree is equal to char
    elif char < tree['root']:
        return return_tree(tree.get('left', {}), word) #checking the left and right subtree to return the right word
    else:
        return return_tree(tree.get('right', {}), word)
    

'''EXIST FUNCTION
    PARAMETERS: TERNARY TREE
                PREFIX OF A WORD
    DEFINITION: A RECURSIVE APPROACH TO CHECK THE EXISTENCE OF A PREFIX IN A WORD'''
def exist_prefix_in_tree(tree:dict,prefix:str) -> bool:
#returning boolean values in this case
    if not prefix:      #if no prefix then return false
        return False

    char = prefix[0]

    if 'root' not in tree:   #if the root is not in the tree, then we will return False 
        return False

    if tree['root'] == char:
        if len(prefix) == 1:
            return True
        return return_tree(tree.get('mid', {}), prefix[1:])  #returning the word from the tree whose prefix matches the prefix we are searching for 
    elif char < tree['root']:
        return return_tree(tree.get('left', {}), prefix) #checking the left subtree
    else:
        return return_tree(tree.get('right', {}), prefix)  #checking the right subtree for the prefix

'''TRAVERSE FUNCTION
    PARAMETERS: TERNARY TREE
                PREFIX OF A WORD
    DEFINITION: A RECURSIVE APPROACH TO OUTPUT ALL THE WORDS BEGINNING FROM THE PREFIX IN THE WORD'''
def autocomplete(tree: dict, prefix: str) -> list:
    if exist_prefix_in_tree(tree,prefix)==False:  #calling the exist prefix in tree function to check if any words prefix matches that word
        a=input('This word does not exist in the tree. Would you like to add it in the dictionary? yes/n')
        if a=='yes':
            insert(tree,prefix)  #inserting the word in the dictionary
        else:
            return False
    suggestions = []  #storing it an empty list 
    subtree=return_tree(tree,prefix)  #getting the subtree from the return tree function after checking the prefix
    result_temp=[]
    traverse(subtree,result_temp)  #traverse over the subtree to find the word
    if exist(tree,prefix)==True:   #if word does exist then append it in the suggestions dictionary
        suggestions.append(prefix)
    for i in result_temp:             
        suggestions.append(prefix+i)

    return suggestions #return the suggestions list

'''HIGHEST FREQUENCE FUNCTION
    PARAMETERS: LIST OF WORDS
                DICTIONARY WITH WORDS AS KEYS AND THEIR FREQUENCY AS VALUE
    DEFINITION: FUNCTION RETURNS THE WORD WITH HIGHEST FREQUENCY '''
def highest_frequency(lst:list,dic:dict):
    res=[]  #empty list
    high=0  #set as our initial lowest value of a word
    for i in lst:   
        if dic[i]>=high:   
            if dic[i]==high:   
                res.append(i)  #appending that index in the empty list when its encountered again/ guessed again/ increased freq
            else:
                res=[i]
            high=dic[i]  
    return res  #returning that list where we are storing those values



        


def main(filename):
    with open(filename) as f:   #defining our whole game in the main function
        lines= f.readlines()

    
    words=[]
    for line in lines:
        line= line.strip()
        words.append(line)

    words=words[1:]
    

    tree = {'root': None, 'right': {}, 'left': {}, 'mid': {},'end_of_word':0}  #how we have defined our TSTs
    for word in words:      #inserting the word into the tree through the insert function
        insert(tree,word)

    #print(tree)

    freq={}
    for item in words:
        freq[item]=0   #starting the frequency of the item as 0, then will keep adding it up when the word gets repeated again


    #How our game is being carried out/the process 
    print("")
    print("HELLO AND WELCOME TO WORD AKINATOR. I CAN READ YOUR MIND. DON'T BELIEVE ME? GIVE IT A TRY!")
    print("HERE IS THE OPERATIONS I CAN DO")
    ch='yes'
    while ch=='yes':
        print("*")
        print("CHOICE 1: PLAY A GUESSING GAME WITH COMPUTER")
        print("CHOICE 2: INSERT A WORD IN YOUR DICTIONARY")
        print("CHOICE 3: DELETE A WORD FROM YOUR DICTIONARY")
        print("CHOICE 4: PRINT ALL WORDS IN YOUR DICTIONARY")
        print("CHOICE 5: CHECK THE EXISTENCE OF A WORD IN YOUR DICTIONARY")
        print("*")
        choice=input("ENTER YOUR CHOICE: ")
        if choice=='1':
            print("*")
            print("THINK OF A WORD. BUT DON'T TELL US YET!")
            prefix= input("Enter a part or prefix of the word: ")
            
            if exist_prefix_in_tree(tree,prefix)=={}:  #if prefix does not match any of the prefixes/words then print the statement
                print('This word does not exist in the tree.')
                
                
            
#calling the autocomplete function and highest frequency for the case of choice 1 to allow the frequency of the guessed word to be incremented
            elif type(autocomplete(tree,prefix))==list:
                result=(autocomplete(tree,prefix))
                final=highest_frequency(result,freq)


                if len(final)>1:
                    print("IS YOUR GUESS IN: ")
                    print(final)
                    confirm=input("YES OR NO? ")
                    if confirm=='yes':
                        think=input("WHAT WAS YOUR WORD? ")
                        freq[think]+=1000
                    elif confirm=='no':
                        think=input("WHAT WAS YOUR WORD? ")
                        insert(tree,think)
                        freq[think]=1
                        print("WORD SUCCESSFULLY INSERTED IN DICTIONARY")

                elif len(final)==1:
                    print("YOUR GUESS IS: ")
                    print(final)
                    confirm=input("YES OR NO? ")
                    if confirm=='no':
                        think=input("WHAT WAS YOUR WORD? ")
                        insert(tree,think)
                        freq[think]=1
                        print("WORD SUCCESSFULLY INSERTED IN DICTIONARY")
            
        #how the rest of the choices are working if chosen
        elif choice=='2':
            print("*")
            inserts=input("ENTER THE WORD YOU WISH TO INSERT ")
            insert(tree,inserts)
            print("SUCCESSFULLY INSERTED")
        elif choice=='3':
            print("*")
            deletes= input("ENTER THE WORD YOU WISH TO DELETE ")
            delete(tree,deletes)
            print("SUCCESSFULLY DELETED")
        elif choice=='4':
            print("*")
            res=[]
            traverse(tree,res)
            print("THE WORDS PRESENT IN THE TREE ARE:")
            for j in res:
                print(j)
        elif choice=='5':
            print("*")
            exists=input("ENTER THE WORD YOU WISH TO CHECK THE EXISTENCE OF ")
            if exist(tree,exists)==True:
                print("{} EXISTS IN THE DICTIONARY".format(exists))
            else:
                print("{} DOES NOT EXISTS IN THE DICTIONARY".format(exists))
                






                
        ch=input("DO YOU WANT TO CONTINUE? yes/no ")

            

main('4000-most-common-english-words-csv.csv')   #using the csv file we used of 4000 words for the words suggestions
tree = {'root': None, 'right': {}, 'left': {}, 'mid': {},'end_of_word':0}


#TEST CASES
# lst=['hello','hell']
# for word in lst:
#     insert(tree,word)

# res=[]
# traverse(tree,res)
# print(res)


# delete(tree,'hello')
# res=[]
# traverse(tree,res)
# print(res)