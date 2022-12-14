import json
import calendar

def read_data(filename):
    try: 
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def write_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

def max_temperature(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]["t"] > x:
                x = data[key]["t"]
    return x

def min_temperature(data, date):
    x = 99999
    for key in data:
        if date == key[0:8]:
            if data[key]["t"] < x:
                x = data[key]["t"]
    return x

def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]["h"] > x:
                x = data[key]["h"]
    return x

def min_humidity(data, date):
    x = 99999
    for key in data:
        if date == key[0:8]:
            if data[key]["h"] < x:
                x = data[key]["h"]
    return x

def tot_rain(data, date):
    x = 0.0
    for key in data:
        if date == key[0:8]:
            x += data[key]["r"]
    return x

def report_daily(data, date):
    display =  "========================= DAILY REPORT ========================\n"
    display += "Date                      Time  Temperature  Humidity  Rainfall\n"
    display += "====================  ========  ===========  ========  ========\n"

    for key in data:
        if date == key[0:8]:
            m = calendar.month_name[int(date[4:6])] + " " + str(int(date[6:8])) + ", " + str(int(date[0:4]))
            time = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            temp = data[key]["t"]
            humid = data[key]["h"]
            rain = data[key]["r"]

            display = display + f'{m:22}{time:8}{temp:13}{humid:10}{rain:10.2f}\n'
    return display

def report_historical(data):
    display =  "============================== HISTORICAL REPORT ===========================\n"
    display += "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    display += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display += "====================  ===========  ===========  ========  ========  ========\n"

    d = ""

    for key in data:
        if d == key[0:8]:
            continue
        else:
            d = key[0:8]
            m = calendar.month_name[int(d[4:6])] + " " + str(int(d[6:8])) + ", " + str(int(d[0:4]))
            mintemp = min_temperature(data = data, date = d)
            maxtemp = max_temperature(data = data, date = d)
            minhum = min_humidity(data = data, date = d)
            maxhum = max_humidity(data = data, date = d)
            totalrain = tot_rain(data = data, date = d)

            display = display + f'{m:20}{mintemp:13}{maxtemp:13}{minhum:10}{maxhum:10}{totalrain:10.2f}\n'
    return display