#Error Module
#By Sanjay(Coconut)
Toggle_Test_1 = False



Error_List = [
"[Nutty] Failed to compile. Check code traceback.", #0
"[Nutty] A false indent has been spotted. Please check traceback.", #1
"[Nutty] A variable has been written in the wrong format. 'set:<name>'", #2
"[Nutty] Found if statement. Parsing now.", #3
"[Nutty] Check if statement. Error.", #4
"[Nutty] Starting Test_Error_List.", #5
"[Nutty] Test_Error_List has concluded.", #6
"[Nutty] <Test Comment>", #7
"[Nutty] Test Failed.", #8
"[Nutty] Undefined Variable.", #9
]

def Test_Error_List():
	if Toggle_Test_1 is True:
		print(Error_List[5])
		print(Error_List[7])
		print(Error_List[6])
	else:
		print(Error_List[8])

#Test_Error_List()