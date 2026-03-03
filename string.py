sentence= "We are always learning new things "
word = (""
        "Music sometimes is boring")
new= sentence+ word
print(sentence)
print(sentence[-1])
print(sentence[0])
print(new)
print(len(new))
print(new.upper())
print(new.lower())
if "fox" in new:
    print(f"fox in the statement")
else:
    print("Not in the statement")
print(new[::-1])
print(new.count('e'))