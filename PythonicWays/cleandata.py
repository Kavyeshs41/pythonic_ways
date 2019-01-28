

with open("E:\dumps\IN\IN.txt") as datafile:
    data = datafile.read()

    COUNTRY_CODE, POSTAL_CODE, PLACE, STATE_NAME, STATE_CODE, STATE_LOCATION, STATE_LOCATION_CODE, COM_NAME, \
    COM_CODE, LAT, LONG, ACC = data.split("\t")
