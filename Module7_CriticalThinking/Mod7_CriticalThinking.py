#Bretts Module 7: Critical Thinking Assignment

RoomNumberDictionary =     {"CSC101":3004, "CSC102":4501, "CSC103":6755, "NET110":1244, "COM241":1411}
InstructorDictionary = {"CSC101":"Haynes", "CSC102":"Alvarado", "CSC103":"Rich", "NET110":"Burke", "COM241":"Lee"}
MeetingTimeDictionary = {"CSC101":"8:00 a.m.", "CSC102":"9:00 a.m.", "CSC103":"10:00 a.m.", "NET110":"11:00 a.m.", "COM241":"1 p.m."}

print("Welcome to Bretts Class information provider! To begin: please enter a course number: ")
userInput = input()

roomNumber = RoomNumberDictionary.get(userInput)
instructor = InstructorDictionary.get(userInput)
meetingTime = MeetingTimeDictionary.get(userInput)

if roomNumber == None or instructor == None or meetingTime == None:
    print("The room you entered is not in the system.")
else:
    print("The class " + userInput + " is in room " + str(roomNumber) + ", instructed by " + str(instructor) + ", and begins at " + str(meetingTime))