delimiter = " # "


asdf = open("itemsHelper.txt",'w')
asdf.seek(0)

exampleLine =  "URL" + delimiter + "Name" + delimiter + "Headline Title" + delimiter + "Location" + delimiter + "Industry" + delimiter + "Overview Current" + delimiter + "Overview Education" + delimiter + "Connections" + delimiter + "School Name 1" + delimiter + "Education Degree 1" + delimiter + "Education Major 1" + delimiter + "Education Time Start 1" + delimiter + "Education Time End 1" + delimiter + "School Name 2" + delimiter + "Education Degree 2" + delimiter + "Education Major 2" + delimiter + "Education Time Start 2" + delimiter + "Education Time End 2" + delimiter + "School Name 3" + delimiter + "Education Degree 3" + delimiter + "Education Major 3" + delimiter + "Education Time Start 3" + delimiter + "Education Time End 3" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter+ "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter

asdf.write(exampleLine)
asdf.close()
