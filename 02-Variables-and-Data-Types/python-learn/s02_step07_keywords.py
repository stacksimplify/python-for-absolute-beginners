# Concept-01: Keywords are reserved words; you cannot use them as names
# Question: Which words are off-limits for using as variable names? (Python's keywords, like if, for, class, True; here is the full list)
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.softkwlist)
print(len(keyword.softkwlist))
total_keywords = len(keyword.kwlist) + len(keyword.softkwlist)
print("Total Python Keywords: ", total_keywords)

# Concept-02: Using a keyword as a name is a SyntaxError; these would not run:
# class = "Math"   # 'class' is reserved
# for = 10         # 'for' is reserved

# Concept-03: Check a word with keyword.iskeyword() (hard keywords) and issoftkeyword() (soft keywords)
# Question-1: How do we check whether a word is a hard keyword, reserved everywhere? (keyword.iskeyword(word) - True for "for" or "class", False for an ordinary name like "name")
# Question-2: How do we check whether a word is a soft keyword, reserved only in some places? (keyword.issoftkeyword(word) - True for "match", False for a hard keyword like "for" or an ordinary word like "city")
import keyword
# Run 1 - iskeyword: hard keywords, reserved everywhere
print("  for:", keyword.iskeyword("for"))
print("  class:", keyword.iskeyword("class"))
print("  name:", keyword.iskeyword("name"))
# Run 2 - issoftkeyword: soft keywords, reserved only in some places (note: "for" is NOT a soft keyword)
print("  match:", keyword.issoftkeyword("match"))
print("  for:", keyword.issoftkeyword("for"))
print("  city:", keyword.issoftkeyword("city"))