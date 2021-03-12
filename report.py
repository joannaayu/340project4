import json
import sys
import texttable


input_file = sys.argv[1]
# domain_dict = {}

output_file = sys.argv[2]


with open(input_file) as input:

    full_dict = json.load(input)
    # print(data)

    domain_table = texttable.Texttable(375)
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


    root_table = texttable.Texttable(75)
    root_table.set_cols_align(["c", "c"])
    root_table.set_cols_valign(["t", "t"])

    server_table = texttable.Texttable(75)
    server_table.set_cols_align(["c", "c"])
    server_table.set_cols_valign(["t", "t"])

    root_table.add_row(["Root CA", "Number of\nOccurences"])
    server_table.add_row(["Web Server", "Number of\nOccurences"])

    root_dict = {}
    server_dict = {}

    for domain in full_dict:
        if full_dict[domain]["root_ca"] == None:
            pass
        elif full_dict[domain]["root_ca"] not in root_dict:
            root_dict[full_dict[domain]["root_ca"]] = 1
        else:
            root_dict[full_dict[domain]["root_ca"]] = root_dict[full_dict[domain]["root_ca"]] + 1

    for domain in full_dict:
        if full_dict[domain]["http_server"] == None or full_dict[domain]["http_server"] == ' ':
            pass
        elif full_dict[domain]["http_server"] not in server_dict:
            server_dict[full_dict[domain]["http_server"]] = 1
        else:
            server_dict[full_dict[domain]["http_server"]] = server_dict[full_dict[domain]["http_server"]] + 1

    new_root_dict = dict(sorted(root_dict.items(), key=lambda item: item[1], reverse = True))
    new_server_dict = dict(sorted(server_dict.items(), key=lambda item: item[1], reverse = True))

    for root_name in new_root_dict:
        row = []
        row.append(root_name)
        row.append(new_root_dict[root_name])
        root_table.add_row(row)

    for server_name in new_server_dict:
        row = []
        row.append(server_name)
        row.append(new_server_dict[server_name])
        server_table.add_row(row)

    # print(server_table.draw())
    # print(root_table.draw())
    # print(domain_table.draw())


# with open('table.txt', 'w') as f:
#     f.write(tabulate(table))

outfile = open(output_file,"w")
outfile.write(domain_table.draw())
outfile.write(root_table.draw())
outfile.write(server_table.draw())
outfile.close()
