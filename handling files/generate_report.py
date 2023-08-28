import csv


def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employe_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employe_file:
        employee_list.append(data)
    return employee_list


employe_list = read_employees('/home/amawan/Python-with-OS/handling files/data/employees.csv')


def proccess_data(employee_list):
    dapartment_list = []
    for dapartment_name in employee_list:
        dapartment_list.append(dapartment_name['Department'])
    dapartment_data = {}
    for dapartment_name in set(dapartment_list):
        dapartment_data[dapartment_name] = dapartment_list.count(dapartment_name)
    return dapartment_data


result = proccess_data(employe_list)


def write_report(dictonary, file):
    with open(file, 'w+') as data:
        for x in sorted(dictonary):
            data.write(str(x) + ":" + str(dictonary[x]) + "\n")
        data.close()


write_report(result, '/home/amawan/Python-with-OS/handling files/data/report.txt')
