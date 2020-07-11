#1
#main.py
from employee import *
def main():
    Aworker=ProductionWorker('','','','','','')
    Aworker.set_id()
    Aworker.set_name()
    Aworker.set_company()
    Aworker.set_vocation()
    Aworker.set_shift()
    Aworker.set_wage()
    print(Aworker)
main()
#2
#main.py
from employee import *
def main():
    A_supervisor=ShiftSupervisor('','','','','','')
    A_supervisor.set_id()
    A_supervisor.set_name()
    A_supervisor.set_company()
    A_supervisor.set_vocation()
    A_supervisor.set_wage_per_year()
    A_supervisor.set_bonus()
    print(A_supervisor)
main()
#3
#main.py
from person import *
def main():
    mycustomer=Customer('','','','','')
    mycustomer.set_name()
    mycustomer.set_tel()
    mycustomer.set_addr()
    mycustomer.set_id()
    mycustomer.set_if()
    print(mycustomer)
main()