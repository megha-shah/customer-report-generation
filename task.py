NEW_LINE = '\n'

NEW_HTML_LINE = '<br>'

def read_data():
    data_file = open("customerdata.txt","r")
    first_row = data_file.readline()
    first_row_list = first_row.split(',')

    phone_details = {}
    tot_orders = 0
    tot_amount = 0
    for line in data_file:
        dic = {}

        if not line.strip():
            continue

        mylist = line.split(',')
        i = 0
        for value in mylist:   
            dic[first_row_list[i].strip()] = value.strip()
            i += 1
        if mylist[1] in phone_details:
            phone_details[mylist[1]].append(dic)
        else:
            listt = [] 
            listt.append(dic)
            phone_details[mylist[1]] = listt  

        tot_orders += 1;
        tot_amount += int(mylist[3])

    data_file.close()
    
    return phone_details, tot_orders, tot_amount


def distribution_of_customers(details):
    order_count = {}
    ordered_once = []
    for key,value in details.iteritems():
        num_of_orders = len(value)

        if num_of_orders == 1:
            ordered_once.append(value[0]['Name'])

        if num_of_orders > 5:
            num_of_orders = 5

        if num_of_orders in order_count:
            order_count[num_of_orders] += 1
        else:
            order_count[num_of_orders] = 1

    return ordered_once, order_count      


def get_customer_distribution(order_count, new_line):
    new_report_str = ''
    new_report_str += 'Distribution of customers: ' + new_line
    for key in order_count:
        if key < 5:
            new_report_str += str(key) + " | " + str(order_count[key]) + new_line
        else:
            new_report_str += "5+ | " + str(order_count[key]) + new_line

    return new_report_str          


def customer_who_orderderd_once(names, new_line):
    new_report_str = ''
    new_report_str += 'Names of the customers who ordered once and did not order again: ' + new_line
    for name in names:
        new_report_str += name + new_line

    return new_report_str    

def save_file(extension, new_line):
    output_file = open('report.' + extension, 'w')

    report_str = ''

    report_str += 'Total number of orders the site received: '
    report_str += str(tot_orders) + new_line + new_line

    report_str += 'Total amount of orders: '
    report_str += str(tot_amount) + new_line + new_line

    report_str += customer_who_orderderd_once(ordered_once, new_line)
    report_str += new_line

    report_str += get_customer_distribution(order_count, new_line)

    if extension == 'html':
        js_file = open('js-code.txt', 'r').read()
        print js_file % 'qqqq'
        HTML_TEMPLATE = open('html-code.txt','r').read()
        report_str = HTML_TEMPLATE % report_str

    output_file.write(report_str)

    output_file.close()

def generate_report(tot_orders, tot_amount, ordered_once, order_count):
    save_file('txt', NEW_LINE)
    save_file('html', NEW_HTML_LINE)



if __name__ == '__main__':
    details, tot_orders, tot_amount = read_data()
    ordered_once, order_count = distribution_of_customers(details)
    generate_report(tot_orders, tot_amount, ordered_once, order_count)
