#Deliveries of melons


def deliveries(data_file):
    """
    Opens the file specified in the argument. It then prints out the number,
    type, and cost of the melons delivered during certain days.
    """
    the_file = open(data_file)
    if data_file == "um-deliveries-20140519.txt":
        print "Day 1"
    elif data_file == "um-deliveries-20140520.txt":
        print "Day 2"
    elif data_file == "um-deliveries-20140521.txt":
        print "Day 3"
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        melon = words[0]
        count = words[-2]
        amount = words[-1]
        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)
    the_file.close()


deliveries("um-deliveries-20140519.txt")
deliveries("um-deliveries-20140520.txt")
deliveries("um-deliveries-20140521.txt")
