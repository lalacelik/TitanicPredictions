
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier

training_set = pd.read_csv("train.csv")
testing_set = pd.read_csv("test.csv")
gender_submissions = pd.read_csv("gender_submission.csv")

# FIRST Group Ages ########################################################
def AgeGrouping(list):
    output=[]
    for x in list:
        if x<=13:output.append("child")
        elif x>= 30:output.append("adult")
        elif x>13 and x<30:output.append("youngad")
        else:output.append("empty")
    return output

training_set['AgeGroup']= AgeGrouping(training_set['Age'])

training_set.to_csv('refactoredtrain.csv', index=False)
trainfrom= pd.read_csv("refactoredtrain.csv")

# #TEST AGE GROUPING##

younga = training_set.loc[(training_set.Age <= 30) & (training_set.Age >= 16)]["Survived"] #DOGRU MU LAN BU
rate_younga = sum(younga)/len(younga)

print("% of younga who survived:", rate_younga)

younga2 = training_set.loc[(training_set.AgeGroup=='youngad')]["Survived"]
rate_younga2 = sum(younga2)/len(younga2)

print("% of younga2 who survived:", rate_younga)

###########################################################################################

Ages= training_set.groupby("AgeGroup")["Survived"].mean()
print ("% of survival by ",Ages)


#CLASS##
Class= training_set.groupby("Pclass")["Survived"].mean()
print ("% of survival by ", Class)

#Class Fare

Fare= training_set.groupby("Pclass")["Fare"].describe()

print ("Fare payment summary by Class", Fare)

#PARCH
Parch= training_set.groupby("Parch")["Survived"].mean()
print ("% survival by PArch",Parch)

#EMBARKED
Embarkment= training_set.groupby(["Embarked"])["Survived"].describe()
print("% survival by dock ",Embarkment)

##Survival percent by multiple factors

SexClass= training_set.groupby(["Sex","Pclass"])["Survived"].mean()
print("% survival by sex and class",SexClass)

AgeSex= training_set.groupby(["Sex", "AgeGroup"])["Survived"].mean()
print("% survival by sex and Age group",AgeSex)

AgeClass= training_set.groupby(["Pclass", "AgeGroup"])["Survived"].mean()
print("% survival by Age group and class",AgeClass)

SexAgeClass= training_set.groupby(["Sex", "Pclass", "AgeGroup"])["Survived"].mean()
print("% survival by sex, age group and class",SexAgeClass)


EmbarkClass= training_set.groupby(["Pclass","Embarked"])["Survived"].mean()#%of survivers
print("% survival by embarkment and class",EmbarkClass)

# FareEmb= training_set.groupby(["Pclass","Embarked"])["Fare"].mean()# average fare per class per embarkment to see how it relates to survival
# print(FareEmb)

##CLASS and Emb better indicator than fare

# EmbarkClassSum= training_set.groupby(["Embarked","Pclass"])["Survived"].sum()#number of survivers
# print(EmbarkClassSum)

#See whether class distribution is similar among embarkments
# EmbarkClass2= training_set.groupby(["Embarked"])["Pclass"].mean()
# print(EmbarkClass2)

#puanlama sistemi yarat
#female olmak ++
 #her kategorinin etki yuzdelerine bak ona gore puanlama sistemi yap
 #en son mainde butun puanlari topla
 #bir cutoff un ustunusurvived olarak isaretle

#####################################################################################
#1 Group ages and check effects
#2 check standard deviations
#plot what you've found
#start points system
##!!! Weight system for points by each



########################################PLOT##########
# # bar plot

# #!!plot survived female number vs dead female number

training_set.groupby(['Sex','AgeGroup'])['Survived'].count().plot(kind='bar')
training_set.groupby(['Sex','AgeGroup', 'Pclass'])['Survived'].size().unstack().plot(kind='bar',stacked=True)

training_set.groupby(['Sex','Survived']).size().unstack().plot(kind='bar', stacked=True)

##!!figure out how to normalize to percentage

training_set.groupby(['Sex','Survived']).size().unstack().plot(kind='bar', stacked=True)

plt.figure(figsize=(5,4), dpi=150)
sns.heatmap(trainfrom.corr(), annot=True)

plt.show()

##TRY WEIGHTS
