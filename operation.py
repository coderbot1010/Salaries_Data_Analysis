import numpy as np
import pandas as pd
from pathlib import Path


def __get_data_frame():
    return pd.read_csv(str(Path.cwd()) + "/Salaries Data Analysis/Salaries.csv")


def define_job_titles():
    print("All Job Titles:")
    titles = dataFrame["JobTitle"].unique()
    # for title in titles:
    #     print(title)
    for i in range(10):
        print(titles[i])
    print("." * 5)
    print("-" * 50)


def get_max_payment():
    print("Maximum Payment", dataFrame["TotalPayBenefits"].max())
    print("Full Info:")
    print(dataFrame[dataFrame["TotalPayBenefits"]
                    == dataFrame["TotalPayBenefits"].max()])
    print("-" * 50)


def get_min_payment():
    print("Minimum Payment", dataFrame["TotalPayBenefits"].min())
    print("Full Info:")
    print(dataFrame[dataFrame["TotalPayBenefits"]
                    == dataFrame["TotalPayBenefits"].min()])
    print("-" * 50)


def get_base_payment_average():
    print("Average Base Payment", dataFrame["BasePay"].mean())
    print("-" * 50)


def get_employee_financial_info(name):
    employee = dataFrame[dataFrame["EmployeeName"] == name]
    print("Base Payment:", employee.loc[employee.index[0], "BasePay"])
    print("Overtime Payments:", employee.loc[employee.index[0], "OvertimePay"])
    print("Benifits Payment:", employee.loc[employee.index[0], "Benefits"])
    print("Other Payment:", employee.loc[employee.index[0], "OtherPay"])
    print("Total Payment:",
          employee.loc[employee.index[0], "TotalPayBenefits"])
    print("-" * 50)


def get_average_payment_per_year():
    print(dataFrame.groupby("Year").mean()['BasePay'])
    print("-" * 50)


print("-" * 50)
# dataFrame = __getDataFrame().dropna()
dataFrame = __get_data_frame().fillna(value=0)
dataFrame.info()
print("-" * 50)
