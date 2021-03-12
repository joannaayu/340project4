import json
import sys
import texttable
import operator


input_file = sys.argv[1]
# domain_dict = {}

output_file = sys.argv[2]


with open(input_file) as input:


    full_dict = json.load(input)

    #DOMAIN TABLE
    domain_table = texttable.Texttable(200)
    domain_table.set_cols_align(["l", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
    domain_table.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t", "t", "t", "t", "t"])
    domain_table.add_row(["Domain", "Scan Time", "IPv4\nAddresses", "IPv6\nAddresses", "HTTP\nServer", "Insecure\nHTTP", "Redirects", "Hosts", "TLS\nVersions", "Root CA", "RDNS Names", "RTT Range", "Geo\nLocations"])

    for domain in full_dict:
        row = []
        row.append(domain)

        for i in full_dict[domain]:

            if full_dict[domain][i] == None:
                row.append("None")
            else:
                row.append(full_dict[domain][i])

        domain_table.add_row(row)


    #RTT RANGE TABLE
    rtt_table = texttable.Texttable(100)
    rtt_table.set_cols_align(["c", "c"])
    rtt_table.set_cols_valign(["c", "t"])
    rtt_table.add_row(["Domain", "RTT Range"])

    rtt_dict = {}
    rtt_empty = {}

    for domain in full_dict:
        if full_dict[domain]["rtt_range"] == None:
            rtt_empty[domain] = None
        else:
            rtt_dict[domain] = full_dict[domain]["rtt_range"]

    rtt_sorted = dict(sorted(rtt_dict.items(), key=lambda i: i[1][0]))

    for d in rtt_empty:
        rtt_sorted[d] = rtt_empty[d]

    for domain in rtt_sorted:
        row = []
        row.append(domain)
        row.append(rtt_sorted[domain])
        print(row)
        rtt_table.add_row(row)

    print(domain_table.draw() + "\n""\n""\n", rtt_table.draw(), file=open(output_file, "w"))
