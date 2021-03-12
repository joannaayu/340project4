import json
import sys
import texttable
import operator


input_file = sys.argv[1]

output_file = sys.argv[2]


with open(input_file) as input:

    full_dict = json.load(input)

    #DOMAIN TABLE-------------------------------------------------------------------------
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


    #RTT RANGE TABLE-------------------------------------------------------------------------
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
        rtt_table.add_row(row)



    #ROOT TABLE AND SERVER TABLE-------------------------------------------------------------------------
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


    #PERCENTAGE TABLE-------------------------------------------------------------------------
    percentage_table = texttable.Texttable(75)
    percentage_table.set_cols_align(["c", "c"])
    percentage_table.set_cols_valign(["t", "t"])
    percentage_table.add_row(["Feature", "Percentage %"])

    percentage_dict = {}

    sslv2 = 0
    sslv3 = 0
    tls1_0 = 0
    tls1_1 = 0
    tls1_2 = 0
    tls1_3 = 0

    insecure = 0
    redirect = 0
    hsts = 0
    ipv6 = 0

    for domain in full_dict:
        if "SSLv2" in full_dict[domain]["tls_versions"]:
            sslv2 += 1

        if "SSLv3" in full_dict[domain]["tls_versions"]:
            sslv3 += 1

        if "TLSv1.0" in full_dict[domain]["tls_versions"]:
            tls1_0 += 1

        if "TLSv1.1" in full_dict[domain]["tls_versions"]:
            tls1_1 += 1

        if "TLSv1.2" in full_dict[domain]["tls_versions"]:
            tls1_2 += 1

        if "TLSv1.3" in full_dict[domain]["tls_versions"]:
            tls1_3 += 1

        if full_dict[domain]["insecure_http"] == True:
            insecure += 1

        if full_dict[domain]["redirect_to_https"] == True:
            redirect += 1

        if full_dict[domain]["hsts"] == True:
            hsts += 1

        if len(full_dict[domain]["ipv6_addresses"]) != 0:
            ipv6 += 1

    total = len(full_dict)

    percentage_dict["SSLv2"] = sslv2/total
    percentage_dict["SSLv3"] = sslv3/total
    percentage_dict["TSSv1.0"] = tls1_0/total
    percentage_dict["TSSv1.1"] = tls1_1/total
    percentage_dict["TSSv1.2"] = tls1_2/total
    percentage_dict["TSSv1.3"] = tls1_3/total
    percentage_dict["Plain HTTP"] = insecure/total
    percentage_dict["HTTPS Redirect"] = redirect/total
    percentage_dict["HSTS"] = hsts/total
    percentage_dict["IPV6"] = ipv6/total

    for feat in percentage_dict:
        row = [feat, (100*percentage_dict[feat])]
        percentage_table.add_row(row)



print(domain_table.draw() + "\n""\n", rtt_table.draw() + "\n""\n", root_table.draw() + "\n""\n", server_table.draw() + "\n""\n", percentage_table.draw() + "\n""\n", file=open(output_file, "w"))
