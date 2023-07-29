lang = ("English", "Arabian", "French", "German", "Spanish")
print(lang)

langList = list(lang)
print(langList)
print(type(langList))

langList.append("Hindi")

lang = tuple(langList)
print(lang)