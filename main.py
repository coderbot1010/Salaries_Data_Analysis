import operation
import visualization

# ----------------------------------------------------- #

operation.define_job_titles()
operation.get_max_payment()
operation.get_min_payment()
operation.get_base_payment_average()
operation.get_average_payment_per_year()

# NATHANIEL FORD
# JOSEPH DRISCOLL
name = input("Enter Employee Name: ")
operation.get_employee_financial_info(name)

# ----------------------------------------------------- #

visualization.plot_base_payment(operation.dataFrame)
visualization.plot_total_payment_with_benifits(operation.dataFrame)
visualization.sacter_plot_base_payment_with_overtime_payment(
    operation.dataFrame)
visualization.regression_plot_base_payment_with_overtime_payment(
    operation.dataFrame)
visualization.heat_map(operation.dataFrame)
