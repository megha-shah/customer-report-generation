NEW_LINE = '\n'

NEW_HTML_LINE = '<br>'

# to read and store data from customerdata.txt file
def read_data():
    data_file = open("customerdata.txt","r")
    first_row = data_file.readline()
    first_row_list = first_row.split(',')

    phone_details = {}
    tot_orders = 0
    tot_amount = 0
    for line in data_file:
        dic = {}

        #ignoring the empty lines
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
    """
        distribution of customers on the basis of their number of orders
    """

    # order_count is a dictionary whose key is order count and value is customer count
    order_count = {}

    # list of name of customers who ordered once 
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
    """
    convert mapping into output format 
    """

    # new_report_str is a string in output format
    new_report_str = ''

    # graph_list is used to store the data of graph for passing in js file
    graph_list = []
    new_report_str += 'Distribution of customers: ' + new_line
    point = []
    point.append("orders_count")
    point.append("customers_count")
    graph_list.append(point)
    for key in order_count:
        #point contains x and y coordinates
        point = []
        if key < 5:
            new_report_str += str(key) + " | " + str(order_count[key]) + new_line
            point.append(str(key))
        else:
            new_report_str += "5+ | " + str(order_count[key]) + new_line
            point.append("5+") 

        point.append(order_count[key])

        graph_list.append(point)    

    return new_report_str, graph_list          


def customer_who_orderderd_once(names, new_line):
    """
    storing the names of customers who ordered once
    """

    new_report_str = ''
    new_report_str += 'Names of the customers who ordered once and did not order again: ' + new_line
    for name in names:
        new_report_str += name + new_line

    return new_report_str 


def save_file(extension, new_line):
    """
    report saving in output file
    """

    output_file = open('report.' + extension, 'w')

    report_str = ''

    # 1.number of orders receive by site
    report_str += 'Total number of orders the site received: '
    report_str += str(tot_orders) + new_line + new_line

    # 2.Total amount of orders
    report_str += 'Total amount of orders: '
    report_str += str(tot_amount) + new_line + new_line

    # 3.Names of customers who oredred once
    report_str += customer_who_orderderd_once(ordered_once, new_line)
    report_str += new_line

    new_report_str, graph_data = get_customer_distribution(order_count, new_line)

    # 4.Grouping of-> count of orders: count of customers
    report_str += new_report_str

    if extension == 'html':

        #6.Adding a bar graph HTML report.
        input_js_file = open('js-code.txt', 'r').read()
        output_js_file = open('report.js', 'w')
        output_js_file.write(input_js_file % graph_data)
        output_js_file.close()

        #5.Generate report as a simple HTML page 
        input_html_file = open('html-code.txt','r').read()
        report_str = input_html_file % report_str

    # if extension is txt, output file is report.txt and if extension is html, output file is report.html
    output_file.write(report_str)

    output_file.close()


def generate_report(tot_orders, tot_amount, ordered_once, order_count):
    """
    generating report 
    """

    save_file('txt', NEW_LINE)
    save_file('html', NEW_HTML_LINE)


if __name__ == '__main__':
    details, tot_orders, tot_amount = read_data()
    ordered_once, order_count = distribution_of_customers(details)
    generate_report(tot_orders, tot_amount, ordered_once, order_count)
