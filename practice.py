from __future__ import print_function
import cobra.test

"not real code, just practice"

model = cobra.test.create_test_model("textbook")
print(len(model.reactions))
atp = model.metabolites.get_by_id("atp_c")
print (atp.name)
print (atp.compartment)
