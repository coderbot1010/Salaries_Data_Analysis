import seaborn as sb
from matplotlib import pyplot as plt


def plot_base_payment(dataFrame):
    sb.distplot(dataFrame["BasePay"])
    plt.show()


def plot_total_payment_with_benifits(dataFrame):
    sb.distplot(dataFrame["TotalPayBenefits"])
    plt.show()


def sacter_plot_base_payment_with_overtime_payment(dataFrame):
    sb.jointplot(x="BasePay", y="OvertimePay", data=dataFrame, kind="scatter")
    plt.show()


def regression_plot_base_payment_with_overtime_payment(dataFrame):
    sb.jointplot(x="BasePay", y="OvertimePay", data=dataFrame, kind="reg")
    plt.show()


def heat_map(dataFrame):
    data = dataFrame.pivot_table(
        values="BasePay", index="JobTitle", columns="Year")
    sb.heatmap(data)
    plt.show()
