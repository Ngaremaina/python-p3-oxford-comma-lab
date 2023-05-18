def oxford_comma(items):
    if len(items) == 0:
      return ""
    
    elif len(items) == 1:
       return items[0]
    
    elif len(items) == 2:
       return f"{items[0]} and {items[1]}"
    
    else:
       string = ', '.join(items[:-1])
       return f"{string}, and {items[-1]}"