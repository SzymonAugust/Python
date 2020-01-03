import matplotlib.pyplot as plt
import numpy as np
import re
from math import fabs

G = 10
LIM_PLOT = 0.25
DENSITY = 0.01
MISTAKE = 0.005          #to count the hit coordinates
DIFFERENCE = 0.05        #in final positions of bullet and target
PLOT_HEIGHT = 15
PLOT_WIDTH = 7.5
CONST = 1000             #control value of primal x0 values 

def main():
    input_strings = np.loadtxt("input.txt", dtype= str, delimiter=";")
    
    size_of_all = input_strings.size
    size_of_one = input_strings[0].size
    number_of_shots = int(size_of_all/size_of_one)
    output_strings = []
    
    for i in range(number_of_shots):
        data_strings = []
        output_line = ""
        
        raw_data_evaluation(data_strings,input_strings[i],size_of_one)
        from_string_to_float(data_strings)
        
        x_cannon = data_strings[0][0]
        y_cannon = data_strings[0][1]
        x_target = data_strings[1][0]
        y_target = data_strings[1][1]
        V_ox = data_strings[2][0]
        V_oy = data_strings[2][1]
        w_x = data_strings[3][0]
        w_y = data_strings[3][1]
        t1 = data_strings[4]
        t2 = data_strings[5]
        t3 = data_strings[6]        
        
        x_of_hit = 0
        y_of_hit = 0
            
        x = [j for j in np.arange(x_cannon-LIM_PLOT, x_target+LIM_PLOT, DENSITY)]
        y = []
        for j in x:
            y.append(polynomial(data_strings[7],j))
                
        x0 = [j for j in np.arange(x_cannon,CONST+DENSITY,DENSITY)]
        y0 = []
        for j in range(0,len(x0)):
            y0.append(y_from_x(x_cannon,y_cannon,V_ox,w_x,V_oy,w_y,x0[j],G))
            if y0[j] - polynomial(data_strings[7],x0[j]) < MISTAKE and j != 0:
                y_of_hit = y0[j]
                x_of_hit = x0[j]
                break
            
        x0 = [j for j in np.arange(x_cannon,x_of_hit+DENSITY,DENSITY)]
        y0 = []
        for j in x0:
            y0.append(y_from_x(x_cannon,y_cannon,V_ox,w_x,V_oy,w_y,j,G))
        
        if (x_of_hit > x_target):
            x = [j for j in np.arange(x_cannon-LIM_PLOT, x_of_hit+LIM_PLOT, DENSITY)]
            y = []
            for j in x:
                y.append(polynomial(data_strings[7],j))
        
        x_of_hit = round(x_of_hit,2)
        y_of_hit = round(y_of_hit,2)
        
        position_of_hit = (x_of_hit,y_of_hit)
        h_max = str(round(np.amax(y0),2))
        V_1 = [round((V_ox+w_x),2), round((velocity_y_from_t(V_oy,G,t1,w_y)),2)]
        V_2 = [round((V_ox+w_x),2), round((velocity_y_from_t(V_oy,G,t2,w_y)),2)]
        V_3 = [round((V_ox+w_x),2), round((velocity_y_from_t(V_oy,G,t3,w_y)),2)]
        hit = is_hit(x_target,y_target,x_of_hit,y_of_hit)
        
        output_line += str(position_of_hit) + ";"
        output_line += " " + str(h_max) + ";"
        output_line += " " + str(V_1) + ";"
        output_line += " " + str(V_2) + ";"
        output_line += " " + str(V_3) + ";"
        output_line += " " + str(hit)
        
        output_strings.append(output_line)
        
        plt.figure(figsize=(PLOT_HEIGHT,PLOT_WIDTH))
        plt.title('Shot no. '+str(i+1))
        plt.ylabel('Y-axis')
        plt.xlabel('X-axis')
        plt.plot(x,y,color="green")
        plt.fill_between(x,y,color="green",interpolate=True)
        plt.plot(x_cannon,y_cannon,'ro',color="red")        
        plt.plot(x0,y0,'r--',color="black")
        plt.plot(x_of_hit,y_of_hit,'ro',color="black")
        plt.plot(x_target,y_target,'ro',color="blue")
        
        plt.savefig(str(i+1)+".png")
    
    np.savetxt("output.txt", output_strings,fmt="%s")

def is_hit(x1,y1,x2,y2):
    if fabs(x1-x2) <= DIFFERENCE and fabs(y1-y2) <= DIFFERENCE:
        return 1
    else:
        return 0

def velocity_y_from_t(velocity, acceleration, time, w_velocity):        #including wind velocity
    return velocity-acceleration*time+w_velocity

def y_from_x(starting_x, starting_y, x_velocity, x_wind_velocity, y_velocity, y_wind_velocity, x, acceleration):
    return (starting_y + (2*(x_velocity+x_wind_velocity)*(y_velocity+y_wind_velocity)*(x-starting_x)-acceleration*np.float_power((x-starting_x),2))/(2*np.float_power((x_velocity+x_wind_velocity),2)))

def polynomial(rates, argument):                    #use elements from list to evaluate polynomial value
    n = len(rates)
    if (n % 2 == 1):
        p_sum = rates[n-1]
    else:
        p_sum = 0
        n += 1
    for i in range(n-2, 0, -2):
        p_sum += rates[i-1]*np.float_power(argument,rates[i])
    return p_sum
    
def cleaning(p):                                 #remove parenthesis, commas and spaces as a first char
    return re.sub("^\s|\]|\[|\,|\(|\)","", p)

def rating(p):                                  #change f(x) into list
    a = re.sub("x\^",",",p)
    a = re.sub("x",", 1",a)
    a = re.sub("\+",",",a)
    a = re.sub("\-",",-",a)
    a = re.sub ("\s","",a)
    return a

def raw_data_evaluation(data,array,size):    #modify whole data input by removing white spaces, split data etc 
    for i in range (size):
        x = cleaning(array[i])
        if i != size-1:             
            x = x.split(" ")
            if len(x) == 1:
                x = x[0]
        else:            
            x = rating(x)
            x = x.split(",")
        data.append(x)
    
def from_string_to_float(array):
    for i in range (len(array)):
        if i < 4 or i == len(array)-1:
            for j in range (len(array[i])):
                array[i][j] = float(array[i][j])
        elif i > 3 and i < len(array)-1:
            array[i] = float(array[i])
main()
