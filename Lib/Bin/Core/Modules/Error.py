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
"[Nutty] Requires a single string as an Argument.", #10
"[Nutty] Closing Shell.", #11
"[Nutty] Shell Exited current Session.", #12
"[Nutty] Compiler requires a path to target file as its single argument.", #13
"[Nutty] Executing file.", #14
"[Nutty] Name needed as first argument. Example: 'credits '", #15
]

Command_List = [
"========================================", #0
"[Nutty] Loading Shell.", #1
"[Nutty] Shell Loaded.", #2
"========================================", #3
"Nutty v1.31.3b (Beta, last updated: Dec/18/2016, 8:58pm est) [Multi-Platform]", #4
"Type [help] for more information.", #5
"========================================", #6
]

#Table check
def Test_Error_List():
	if Toggle_Test_1 is True:
		print(Error_List[5])
		print(Error_List[7])
		print(Error_List[6])
	else:
		print(Error_List[8])

#Test_Error_List()
