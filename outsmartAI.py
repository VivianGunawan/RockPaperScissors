import numpy as np
from selenium import webdriver

driver=webdriver.Chrome()
url="http://www.essentially.net/rsp/end.jsp"
driver.get(url)

#Takes in a number and returns the string rock, paper or scissor
def lexicon(n):
    if(n==0):
        return "Rock"
    if(n==1):
        return "Paper"
    if(n==2):
        return "Scissor"
    
def lexicon_ai(s):
    if(s=="Rock"):
        return 0
    if(s=="Paper"):
        return 1
    if(s=="Scissor"):
        return 2

def lexicon_result(outcome):
    if (outcome == "We tied."):
        return 2
    if (outcome =="You lost."):
        return 0
    if (outcome =="You won."):
        return 1
Me=[]
AI=[]
wins=[]
   
def play(iterations):
    Me.clear()
    AI.clear()
    wins.clear()
    i=0
    while i<iterations:
        n=np.random.randint(0,2)
#        if n==0:
        turn()
 #       else:
#            smart_turn()
        i+=1
   
def turn():
    Rock = driver.find_element_by_name('rock')
    Paper = driver.find_element_by_name('paper')
    Scissor = driver.find_element_by_name('scissor')
    n=np.random.randint(0,3)
    if n==0:
        Rock.click()
    if n==1:
        Paper.click()
    if n==2:
        Scissor.click()
    Me.append(n)
    computer_play = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td[3]/font/b")
    outcome=driver.find_element_by_xpath("/html/body/h3[2]/blockquote")
    AI.append(lexicon_ai(computer_play.text))
    wins.append(lexicon_result(outcome.text))
    
def smart_turn():
    Rock = driver.find_element_by_name('rock')
    Paper = driver.find_element_by_name('paper')
    Scissor = driver.find_element_by_name('scissor')
    n=[i for i in range(0,len(wins)) if wins[i]==1]
    winning_AI=[AI[i+1] for i in range(0,len(n)-1)]
    counter=[winning_AI.count(0),winning_AI.count(1),winning_AI.count(2)]
    counter_me=[Me.count(0),Me.count(1),Me.count(2)]
    if min(counter_me)>min(counter):
        x=counter_me.index(min(counter_me))
    else:
        x=counter.index(min(counter))
    if x==0:
        Paper.click()
    if x==1:
        Scissor.click()
    if x==2:
        Rock.click()
    Me.append(x)
    computer_play = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td[3]/font/b")
    outcome=driver.find_element_by_xpath("/html/body/h3[2]/blockquote")
    AI.append(lexicon_ai(computer_play.text))
    wins.append(lexicon_result(outcome.text))
    
    


def test(n):
    for i in range(n):
        play(100)
        endgame=driver.find_element_by_xpath("/html/body/form[2]/input")
        endgame.click()
        winloss=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]/tt/b/font")
        print("My win/loss ratio for game",i+1,"=",winloss.text)
        newgame=driver.find_element_by_xpath("/html/body/form/input")
        newgame.click() 
test(10)
