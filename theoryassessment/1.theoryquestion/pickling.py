# Pickling in Python

import pickle

# Python object
my_list = [11, 'Python', b'pickling test']

# Pickling
with open("data.pickle","wb") as file_handle:
    pickle.dump(my_list, file_handle, pickle.HIGHEST_PROTOCOL)

print("Pickling completed!")