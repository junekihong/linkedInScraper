delimiter = " # "


asdf = open("itemsHelper.txt",'w')
asdf.seek(0)

exampleLine = "Name" + delimiter + "Headline Title" + delimiter + "Location" + delimiter + "Industry" + delimiter + "Overview Current" + delimiter + "Overview Education" + delimiter + "Connections" + delimiter + "Experience Title 1" + delimiter + "Time Began 1" + delimiter + "Time Ended 1" + delimiter + "Duration 1" + delimiter + "Experience Title 2" + delimiter + "Time Began 2" + delimiter + "Time Ended 2" + delimiter + "Duration 2" + delimiter + "Experience Title 3" + delimiter + "Time Began 3" + delimiter + "Time Ended 3" + delimiter + "Duration 3" + delimiter + "Experience Title 4" + delimiter + "Time Began 4" + delimiter + "Time Ended 4" + delimiter + "Duration 4" + delimiter + "Experience Title 5" + delimiter + "Time Began 5" + delimiter + "Time Ended 5" + delimiter + "Duration 5" + delimiter 

asdf.write(exampleLine)
asdf.close()
