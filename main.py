# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import matplotlib.pyplot as plt

training_set = pd.read_csv("train.csv")
testing_set = pd.read_csv("test.csv")
gender_submissions = pd.read_csv("gender_submission.csv")

#training set ideki survivali predict etmek

#Rates of Survival

##FROM TUTORIAL ON KAGGLE

women = training_set.loc[training_set.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)


# According to AGE
# FIRST group ages
def AgeGrouping(list):
    output=[]
    for x in list:
        if x<=13:output.append("child")
        elif x>= 30:output.append("adult")
        elif x is None:output.append("empty")
        else:output.append("youngad")
    return output

training_set['AgeGroup']= AgeGrouping(training_set['Age'])

# #TEST AGE GROUPING
younga = training_set.loc[(training_set.Age <= 30) & (training_set.Age >= 16)]["Survived"] #DOGRU MU LAN BU
rate_younga = sum(younga)/len(younga)

print("% of younga who survived:", rate_younga)


younga2 = training_set.loc[(training_set.AgeGroup=='youngad')]["Survived"]
rate_younga2 = sum(younga2)/len(younga2)

print("% of younga2 who survived:", rate_younga)

######
Ages= training_set.groupby("AgeGroup")["Survived"].mean()
print (Ages)

# emptyage = training_set.loc[training_set.AgeGroup== 'empty']["Survived"] #DOGRU MU LAN BU
# rate_empty = sum(emptyage)/len(emptyage)
#
# print("% of emptyage who survived:", rate_empty)

#CLASS
Class= training_set.groupby("Pclass")["Survived"].mean()
print (Class)

#PARCH
Parch= training_set.groupby("Parch")["Survived"].mean()
print (Parch)

##kesisimlere bak female children female first class vidi vidi

Class= training_set.groupby("Pclass")["Survived"].mean()
print (Class)

SexClass= training_set.groupby(["Sex","Pclass"])["Survived"].mean()
print(SexClass)

AgeSex= training_set.groupby(["Sex", "AgeGroup"])["Survived"].mean()
print(AgeSex)

AgeClass= training_set.groupby(["Pclass", "AgeGroup"])["Survived"].mean()
print(AgeClass)

SexAgeClass= training_set.groupby(["Sex", "Pclass", "AgeGroup"])["Survived"].mean()
print(SexAgeClass)

####
## Now Check SDev

AgeDev= training_set['Age'].std()
print("Standard Deviation of age", AgeDev)

#puanlama sistemi yarat
#female olmak ++
 #her kategorinin etki yuzdelerine bak ona gore puanlama sistemi yap
 #en son mainde butun puanlari topla
 #bir cutoff un ustunusurvived olarak isaretle

#####################################################################################
#1 Group ages and check effects
#2 check standard deviationss
#plot what you've found
#start points system


# bar plot
training_set.plot(kind='bar',
        x='Sex',
        y='Survived',
        color='green')

##NEED summary version of above

# set the title
plt.title('BarPlot')

# show the plot
plt.show()