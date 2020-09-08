import csv
    
def insertInto (session, filename, table_name, column_names):
    """
    This funtion is created to insert data into database table from the csv
    :param cassandra-session session: Current database session
    :param str filename: data from csv
    :param str table_name: table name to be edited
    :param Tuple[str] column_names: columns from csv
    :return nothing
    :rtype None
    """
    
    columnLoc = "%s, "*len(column_names)
    columnLocCorrect = f"({columnLoc[:-2]})"
    columns_in_query = "(" + ', '.join(column_names) + ")"
    with open(filename, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        header_row = next(csvreader)
        index = {name:index for index,name in enumerate(header_row)}
        for line in csvreader:
                query = f"INSERT INTO {table_name} "
                query = query + f"{columns_in_query} VALUES {columnLocCorrect}"
                data_values = getData(line, column_names, index)
                session.execute(query, data_values)
    print(f"Data inserting into {table_name} completed.")