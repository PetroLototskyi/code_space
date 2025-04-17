
def encodeString(stringVal):
    # Your code goes here.
    encoding=[]
    count = 1
    prevChar = None
    for char in stringVal:
        
        if char != prevChar:
            if prevChar is not None:
                encoding.append((prevChar, count))
            count =1
            # print(f'New character is {char}')
            prevChar = char      
        else:
            count+=1
    if prevChar is not None:
        encoding.append((prevChar, count))
        
        # print(encoding[0][1])
    return encoding
    

def decodeString(encodedList):
    # Your code goes here.
    str=""
    for element, count in encodedList:
        str+=element*count
    
    return str

art =  '''                                                                    
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''

encoded =encodeString(art)
decoded = decodeString(encoded)

print(encoded)

print(decoded)