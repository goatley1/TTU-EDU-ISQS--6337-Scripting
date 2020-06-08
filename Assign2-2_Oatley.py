#Creator:  Aaron Oatley
#Date:  2020.06.05
#Assignment 2-2



#Declare global variables
speed = float(input('How fast is the train going in miles per hour?'))
time = int(input('How long has the train been traveling in hours?'))
distance = 0


#set output headers
print('\n')
print('Hour\tDistance')
print('-----------------------')

#define function to calculate distance and print output

def fun(speed, time):
	for t in range(time):
		distance = (t+1) * speed
		print(t+1,'\t   ',distance)
		
#execute defined function
fun(speed,time)		