import json
import sys
import texttable


input_file = sys.argv[1]
# domain_dict = {}

output_file = sys.argv[2]


with open(input_file) as input:


    full_dict = json.load(input)
    # print(data)

    domain_table = texttable.Texttable(0)
    # domain_table.set_cols_align(["l", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
    # domain_table.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t", "t", "t", "t", "t"])
    # domain_table.add_row(["Domain", "Scan Time", "IPv4\nAddresses", "IPv6\nAddresses", "HTTP\nServer", "Insecure\nHTTP", "Redirects", "Hosts", "TLS\nVersions", "Root CA", "RDNS Names", "RTT Range", "Geo\nLocations"])

    domain_table.set_cols_align(["l", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
    domain_table.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t", "t"])
    domain_table.add_row(["Domain", "Scan Time", "IPv4\nAddresses", "IPv6\nAddresses", "HTTP\nServer", "Insecure\nHTTP", "Redirects", "TLS\nVersions", "Root CA", "Geo\nLocations"])

    for domain in full_dict:
        row = []
        row.append(domain)

        for i in full_dict[domain]:

            if full_dict[domain][i] == None:
                row.append("None")

            elif isinstance(full_dict[domain][i], list) == True:
                for l in full_dict[domain][i]:


            else:
                row.append(full_dict[domain][i])

        print(row)

        domain_table.add_row(row)


    out_file = open(output_file, "w")




    # print (domain_table.draw())
          # for domain in full_dict:


        # dict = json.loads(input)
        # print(dict)
