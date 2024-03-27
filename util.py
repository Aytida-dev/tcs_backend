def convertTODict(columnArray , resultArray):
    column_names = [i[0] for i in columnArray] 
    result_with_column_names = []

    for row in resultArray:
      result_with_column_names.append(dict(zip(column_names, row)))
        
    return result_with_column_names