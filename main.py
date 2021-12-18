# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import explore

##FROM TUTORIAL ON KAGGLE#################


women = explore.training_set.loc[explore.training_set.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)

explore.testing_set['AgeGroup']= explore.AgeGrouping(explore.testing_set['Age'])
explore.training_set.to_csv('refactoredtest.csv', index=False)
testfrom= explore.pd.read_csv("refactoredtest.csv")


y = explore.trainfrom["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch", "AgeGroup"]
X = explore.pd.get_dummies(explore.trainfrom[features])
X_test = explore.pd.get_dummies(explore.trainfrom[features])

model = explore.RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = explore.pd.DataFrame({'PassengerId': testfrom.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")


####################SURVIVAL##################



#training set ideki survivali predict etmek

#Rates of Survival


#

# SurviverAge= training_set.loc["Survived"]

# According to AGE
