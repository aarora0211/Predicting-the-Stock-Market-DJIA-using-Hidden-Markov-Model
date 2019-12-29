'''
Akshit Arora, Sheershak Agarwal
DataSet.py
    Predicting the stock market based on the DJIA relative percentage increase/decrease
    The dataset contains the Dow Jones Industrial Average
    recorded every week from 01/06/2012 until 08/29/2017.
    The dataset is a modified version of the below link
    Link: https://data.world/chasewillden/stock-market-from-a-high-level
'''

import csv

Dow_Jones_Dict = {}
with open("DowJones.csv",'rt') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        Dow_Jones_Dict[row[0]] = row[2]

'''Hidden States
   S1: Low = -2.0 or below [-inf, -2.0)
   S2: Moderate Low = -0.5 to -2.0 (both inclusive) [-0.5, -2.0]
   S3: Normal = -0.5 to 0.5 (both exclusive) (-0.5, 0.5)
   S4: Morerate High = 0.5 to 2.0 (both exclusive) [0.5, 2.0]
   S5: High = 2.0 or high (2.0, inf]
'''
states = ('Low', 'Moderate_Low', 'Normal', 'Moderate_High', 'High')
obs = ('Invest', 'Do_Not_Invest', 'Your_Choice')

start_prob = {} #The starting probability
Low = 0
Moderate_Low = 0
Normal = 0
Moderate_High = 0
High = 0

tranition_transformation = [];

#Calculating the start probability
for vals in Dow_Jones_Dict:
    temp_val = Dow_Jones_Dict[vals]
    temp_val = float(temp_val)
    if (temp_val < -2.0):
        Low += 1
        tranition_transformation.append("Low");
    elif (temp_val >= -2.0 and temp_val <= -0.5):
        Moderate_Low += 1
        tranition_transformation.append("Moderate_Low");
    elif (temp_val > -0.5 and temp_val < 0.5):
        Normal += 1
        tranition_transformation.append("Normal");
    elif (temp_val > 0.5 and temp_val < 2.0):
        Moderate_High += 1
        tranition_transformation.append("Moderate_High");
    else:
        High += 1
        tranition_transformation.append("High");

start_prob["Low"] = Low/len(Dow_Jones_Dict)
start_prob["High"] = High/len(Dow_Jones_Dict)
start_prob["Normal"] = Normal/len(Dow_Jones_Dict)
start_prob["Moderate_Low"] = Moderate_Low/len(Dow_Jones_Dict)
start_prob["Moderate_High"] = Moderate_High/len(Dow_Jones_Dict)

#Calculate the transition probability: Yet to do
transition_prob = {
    'Low' : {'Low': 0, 'Moderate_Low': 0,'Normal':0,'Moderate_High':0,'High':0},
    'High' : {'Low': 0, 'Moderate_Low': 0,'Normal':0,'Moderate_High':0,'High':0},
    'Normal': {'Low': 0, 'Moderate_Low': 0,'Normal':0,'Moderate_High':0,'High':0},
    'Moderate_Low':{'Low': 0, 'Moderate_Low': 0,'Normal':0,'Moderate_High':0,'High':0},
    'Moderate_High':{'Low': 0, 'Moderate_Low': 0,'Normal':0,'Moderate_High':0,'High':0},
}

for i in range(0,len(Dow_Jones_Dict) - 1):
    transition_prob[tranition_transformation[i]][tranition_transformation[i+1]]+=1

state_prob = {
    'Low' : 0,
    'High' : 0,
    'Normal': 0,
    'Moderate_Low':0,
    'Moderate_High':0,
}

for i in state_prob:
    sum_row = 0
    temp = transition_prob[i]
    for j in temp:
        sum_row += temp[j]
    state_prob[i] = sum_row

for i in transition_prob:
    for j in transition_prob:
        transition_prob[i][j] = transition_prob[i][j]/state_prob[i]

#Emission Probability
emission_prob = {
    'Low' : {'Invest': 0.0, 'Do_Not_Invest': 0.8,'Your_Choice':0.2},
    'High' : {'Invest': 0.8, 'Do_Not_Invest': 0.0,'Your_Choice':0.2},
    'Normal': {'Invest': 0.25, 'Do_Not_Invest': 0.25,'Your_Choice':0.5},
    'Moderate_Low':{'Invest': 0.3, 'Do_Not_Invest': 0.4,'Your_Choice':0.3},
    'Moderate_High':{'Invest': 0.4, 'Do_Not_Invest': 0.3,'Your_Choice':0.3},
}
