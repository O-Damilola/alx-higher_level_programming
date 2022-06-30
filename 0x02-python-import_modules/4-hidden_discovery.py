#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid_4
    jane = []
    for i in dir(hid_4):
        if i.startswith('_'):
            continue
        else:
            jane.append(i)
    for x in jane:
        print(x)
