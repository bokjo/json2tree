# Pseudo code

1. Parse the JSON file into single variable
1. Loop over the JSON object (dictionary) [first  Level 1 | key - value]
   1. If the `value` of the current `key` is of type dictionary or list create new element in the treeview with name/identifier same the `key` but keep the value of the previous parent(or default to the main default one!) and loop over the new dictionary or list and do the same as above while creating new elements in the tree...
   2. If the `value` of the current `key` is just a simple string or number create a parent with name as the `key` and append a child to it with the simple string or number value... and continue to the next key...
1. Repeat until all the keys are looped over
