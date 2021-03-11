import geoip2.database

#from https://geoip2.readthedocs.io/en/latest/

def get_locations(ipv4):

    locations = []

    for i in range(len(ipv4)):

        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ipv4[i])

        try:
            city = response.city.name + ', '

        except:
            city = ''
            pass

        try:
            province = city + response.subdivisions.most_specific.name + ', '

        except:
            province = ''
            pass

        try:
            final_loc = province + response.country.name

            if len(locations) == 0:
                locations = [final_loc]

            else:
                if final_loc in locations:
                    pass

                else:
                    locations = locations + [final_loc]

        except:
            pass

        reader.close()

    return locations
