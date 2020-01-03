import matplotlib.pyplot as plt
import numpy as np
import re
from math import fabs

DIFFERENCE = 0.2
DENSITY = 0.1
GATE = 1
G = 10
ICE_HEIGHT = 40
ICE_WIDTH = 60
PLOT_HEIGHT = 15
PLOT_WIDTH = 7.5

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
        print(data_strings)
        
        x_o = data_strings[0][0]
        y_o = data_strings[0][1]
        m = data_strings[1]
        r = data_strings[2]
        u = data_strings[3]
        V_ox = data_strings[4][0]
        V_oy = data_strings[4][1]
        V_o = velocity(V_ox,V_oy)
        
        is_out = 0
        
        a = u*G
        if V_o != 0:
            a_x = V_ox/V_o*a
            a_y = V_oy/V_o*a
            t = V_o/a
        else:
            a_x = 0
            a_y = 0
            t = 0
        t0 = 0
        V_x = V_ox
        V_y = V_oy
        x = x_o
        y = y_o
        alt_x = pos_final(x_o,V_ox,a_x)
        alt_y = pos_final(y_o,V_oy,a_y)
        trajectory = [[],[]]
        middle_position = [[],[]]      
        trajectory[0].append(x_o)
        trajectory[1].append(y_o)
        middle_position[0].append(x_o)
        middle_position[1].append(y_o)
        
        while (is_out == 0):
            direction = which_direction(V_x,V_y)
            if direction == "NE" and (is_in_rink(alt_x-r,alt_y-r)):
                trajectory[0].append(alt_x-r)
                trajectory[1].append(alt_y-r)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            elif direction == "NW" and (is_in_rink(alt_x+r,alt_y-r)):
                trajectory[0].append(alt_x+r)
                trajectory[1].append(alt_y-r)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            elif direction == "SE" and (is_in_rink(alt_x-r,alt_y+r)):
                trajectory[0].append(alt_x-r)
                trajectory[1].append(alt_y+r)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            elif direction == "SW" and (is_in_rink(alt_x+r,alt_y+r)):
                trajectory[0].append(alt_x+r)
                trajectory[1].append(alt_y+r)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            elif direction == "N" and (is_in_rink(alt_x,alt_y-r)):
                trajectory[0].append(alt_x)
                trajectory[1].append(alt_y-r)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            elif direction == "E" and (is_in_rink(alt_x-r,alt_y)):
                trajectory[0].append(alt_x-r)
                trajectory[1].append(alt_y)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            elif direction == "S" and (is_in_rink(alt_x,alt_y+r)):
                trajectory[0].append(alt_x)
                trajectory[1].append(alt_y+r)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            elif direction == "W" and (is_in_rink(alt_x+r,alt_y)):
                trajectory[0].append(alt_x+r)
                trajectory[1].append(alt_y)
                middle_position[0].append(alt_x)
                middle_position[1].append(alt_y)
                break
            else:
                tmp_V_x = V_x
                tmp_V_y = V_y
                tmp_x = x
                tmp_y = y
                if len(direction) == 2:
                    if direction == "NE":
                        x_t = x - r
                        y_t = y - r
                        V_x = final_velocity(tmp_V_x,a_x,ICE_WIDTH,x)
                        V_y = final_velocity(tmp_V_y,a_y,ICE_HEIGHT,y)
                    elif direction == "NW":
                        x_t = x + r
                        y_t = y - r
                        V_x = (-1)*final_velocity(tmp_V_x,a_x,0,x)
                        V_y = final_velocity(tmp_V_y,a_y,ICE_HEIGHT,y)
                    elif direction == "SE":
                        x_t = x - r
                        y_t = y + r
                        V_x = final_velocity(tmp_V_x,a_x,ICE_WIDTH,x)
                        V_y = (-1)*final_velocity(tmp_V_y,a_y,0,y)
                    elif direction == "SW":
                        x_t = x + r
                        y_t = y + r
                        V_x = (-1)*final_velocity(tmp_V_x,a_x,0,x)
                        V_y = (-1)*final_velocity(tmp_V_y,a_y,0,y)
                    t1 = (tmp_V_x-V_x)/a_x
                    t2 = (tmp_V_y-V_y)/a_y
                    tmp_t = min(t1,t2)
                    t0 += tmp_t     
                    x = pos(x,tmp_V_x,a_x,tmp_t)
                    y = pos(y,tmp_V_y,a_y,tmp_t)
                    if direction == "NE":
                        x_t = x - r
                        y_t = y - r
                    elif direction == "NW":
                        x_t = x + r
                        y_t = y - r
                    elif direction == "SE":
                        x_t = x - r
                        y_t = y + r
                    elif direction == "SW":
                        x_t = x + r
                        y_t = y + r
                    if (t1 < t2):
                        a_x = -a_x
                        V_x = -V_x
                        V_y = signum(tmp_V_y)*final_velocity(tmp_V_y,a_y,y,tmp_y)
                    else:
                        a_y = -a_y
                        V_y = -V_y
                        V_x = signum(tmp_V_x)*final_velocity(tmp_V_x,a_x,x,tmp_x)
                elif len(direction) == 1:
                    if direction == "N":
                        x_t = x
                        y_t = y - r
                        V_y = final_velocity(tmp_V_y,a_y,ICE_HEIGHT,y)
                        tmp_t = (tmp_V_y-V_y)/a_y
                        y = pos(y,tmp_V_y,a_y,tmp_t)
                    elif direction == "W":
                        x_t = x + r
                        y_t = y
                        V_x = (-1)*final_velocity(tmp_V_x,a_x,0,x)
                        tmp_t = (tmp_V_x-V_x)/a_x
                        x = pos(x,tmp_V_x,a_x,tmp_t)
                    elif direction == "E":
                        x_t = x - r
                        y_t = y
                        V_x = final_velocity(tmp_V_x,a_x,ICE_WIDTH,x)
                        tmp_t = (tmp_V_x-V_x)/a_x
                        x = pos(x,tmp_V_x,a_x,tmp_t)
                    elif direction == "S":
                        x_t = x
                        y_t = y + r
                        V_y = (-1)*final_velocity(tmp_V_y,a_y,0,y)
                        tmp_t = (tmp_V_y-V_y)/a_y
                        y = pos(y,tmp_V_y,a_y,tmp_t)
                    t0 += tmp_t
                    if direction == "N":
                        y_t = y - r
                        a_y = -a_y
                        V_y = -V_y
                    elif direction == "W":
                        x_t = x + r
                        a_x = -a_x
                        V_x = -V_x
                    elif direction == "E":
                        x_t = x - r
                        a_x = -a_x
                        V_x = -V_x
                    elif direction == "S":
                        y_t = y + r
                        a_y = -a_y
                        V_y = -V_y
                else:
                    break
                    
                alt_x = pos_final(x,V_x,a_x)
                alt_y = pos_final(y,V_y,a_y)
                if (is_in_gate(x_t,y_t,DIFFERENCE)):
                    is_out = 1 
                trajectory[0].append(x_t)
                trajectory[1].append(y_t)
                middle_position[0].append(x)
                middle_position[1].append(y)
                    
        x_ice_1 = [i for i in np.arange(0,ICE_WIDTH+DENSITY,DENSITY)]
        y_ice_1 = [i for i in np.arange(0,(ICE_HEIGHT-GATE)/2+DENSITY,DENSITY)]
        y_ice_2 = [i for i in np.arange((ICE_HEIGHT+GATE)/2,ICE_HEIGHT+DENSITY,DENSITY)]
        x_ice_2 = []
        x_ice_3 = []
        y_ice_3 = []
        y_ice_4 = []
        for j in range(len(x_ice_1)):
            y_ice_3.append(0)
            y_ice_4.append(ICE_HEIGHT)
        for j in range(len(y_ice_1)):
            x_ice_2.append(0)
            x_ice_3.append(ICE_WIDTH)
            
        n = len(trajectory[0]) 
        if (is_in_gate(trajectory[0][n-1],trajectory[1][n-1],DIFFERENCE)):
            t = t0
        plt.figure(figsize=(PLOT_HEIGHT,PLOT_WIDTH))
        plt.title("Trajectory no. " + str(i+1))
        plt.axis('off')
        plt.plot(x_ice_1,y_ice_3,color="black")
        plt.plot(x_ice_1,y_ice_4,color="black")
        plt.plot(x_ice_2,y_ice_1,color="black")
        plt.plot(x_ice_3,y_ice_1,color="black")
        plt.plot(x_ice_2,y_ice_2,color="black")
        plt.plot(x_ice_3,y_ice_2,color="black")
        plt.plot(trajectory[0],trajectory[1],'r--',color="red")
        plt.plot(trajectory[0][n-1],trajectory[1][n-1],'ro',color='blue')
        
        size = len(middle_position[0])
        
        if is_out:
            output_line += "*(out)*"+";"
        else:
            output_line += "("+str(round(middle_position[0][size-1],2))+", "+str(round(middle_position[1][size-1],2))+");"
        
        output_line += " " + str(round(t,2))
        
        for j in range(1,size-1):
            if round(middle_position[0][j],2) == 0:
                middle_position[0][j] = fabs(round(middle_position[0][j],2))
            if round(middle_position[1][j],2) == 0:
                middle_position[1][j] = fabs(round(middle_position[1][j],2))
            output_line += "; ("+str(round(middle_position[0][j],2))+", "+str(round(middle_position[1][j],2))+")"
        
        output_strings.append(output_line)
        
        plt.savefig(str(i+1)+".png")
    
    np.savetxt("output.txt", output_strings,fmt="%s")
        
def signum(p):
    if p > 0:
        return 1
    elif p < 0:
        return -1
    else:
        return 0
def is_in_rink(x,y):
    if x > 0 and x < ICE_WIDTH and y > 0 and y < ICE_HEIGHT:
        return 1
    else:
        return 0

def is_in_gate(x,y,dif):
    if fabs(x) <= dif or fabs(x-ICE_WIDTH) <= dif:
        if y >= (ICE_HEIGHT-GATE)/2 and y <= (ICE_HEIGHT+GATE)/2:
            return 1
    else:
        return 0

def pos_final(z_o,V_o,a):
    if a == 0:
        return z_o
    else:
        return z_o + np.float_power(V_o,2)/(2*a)

def pos(z_o,V_o,a,t):
    return z_o + + V_o*t - np.float_power(t,2)*a/2
        
def velocity(v_x,v_y):
    return np.sqrt(np.float_power(v_x,2)+np.float_power(v_y,2))

def final_velocity(v_o,a,z,z_o):
    if (np.float_power(v_o,2)-2*a*(z-z_o)) < 0:
        return 0
    else:
        return np.sqrt(np.float_power(v_o,2)-2*a*(z-z_o))
            
def which_direction(v_x,v_y):
    if v_x != 0 and v_y != 0:
        if v_x > 0:
            if v_y > 0:
                return 'NE'
            else:
                return 'SE'
        else:
            if v_y > 0:
                return 'NW'
            else:
                return 'SW'
    elif v_x == 0 and v_y != 0:
        if v_y > 0:
            return "N"
        else:
            return "S"
    elif v_x != 0 and v_y == 0:
        if v_x > 0:
            return "E"
        else:
            return "W"  
    else:
        return ""
    
def cleaning(p):                                 #remove parenthesis, commas and spaces as a first char
    return re.sub("^\s|\]|\[|\,|\(|\)","", p)

def raw_data_evaluation(data,array,size):    #modify whole data input by removing white spaces, split data etc 
    for i in range (size):
        x = cleaning(array[i])    
        x = x.split(" ")
        if len(x) == 1:
            x = x[0]
        data.append(x)
        
def from_string_to_float(array):
    for i in range (len(array)):
        if i == 0 or i == 4:
            for j in range (len(array[i])):
                array[i][j] = float(array[i][j])
        else:
            array[i] = float(array[i])
        
main()
