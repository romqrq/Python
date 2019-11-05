{"changed":true,"filter":false,"title":"assertions.py","tooltip":"/assertions.py","value":"","undoManager":{"mark":0,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":29},"action":"insert","lines":["def count_upper_case(message):","    count = 0","    for c in message:","        if c.isupper():","            count += 1","    return count","","assert count_upper_case(\"\") == 0, \"Empty string\"","assert count_upper_case(\"A\") == 1, \"One upper case\"","assert count_upper_case(\"a\") == 0, \"One lower case\"","assert count_upper_case(\"£$%%^\") == 0, \"Special characters\"","","print(\"All the tests passed\")"],"id":1}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":6},"action":"insert","lines":["# "],"id":2},{"start":{"row":2,"column":4},"end":{"row":2,"column":6},"action":"insert","lines":["# "]},{"start":{"row":3,"column":4},"end":{"row":3,"column":6},"action":"insert","lines":["# "]},{"start":{"row":4,"column":4},"end":{"row":4,"column":6},"action":"insert","lines":["# "]},{"start":{"row":5,"column":4},"end":{"row":5,"column":6},"action":"insert","lines":["# "]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "],"id":3}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":51},"action":"insert","lines":["return sum([1 for c in message if c.isupper()])"],"id":4}],[{"start":{"row":6,"column":51},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":4},"end":{"row":7,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572880400999}