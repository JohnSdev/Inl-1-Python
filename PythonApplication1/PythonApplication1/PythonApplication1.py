data="Hello\n World"
for enum in data:
    if enum == "\":
        data2 = data[:enum] + "\" + data[enum:]
print(data2)
