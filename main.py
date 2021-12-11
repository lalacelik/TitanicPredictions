# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
training_set = pd.read_csv("train.csv")
testing_set = pd.read_csv("test.csv")
gender_submissions = pd.read_csv("gender_submission.csv")


#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
#
# print ("Hello")
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
