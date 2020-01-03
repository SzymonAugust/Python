import matplotlib.pyplot as plt
import numpy as np
import re
from math import fabs

DIFFERENCE = 0.03
DENSITY = 0.01
ENERGY_LEFT = 0.7
COF = 0.015                     #coefficient of friction
GATE = 1
G = 9.81
R = 0.03
D = 0.1
TABLE_HEIGHT = 1.35
TABLE_WIDTH = 2.7
PERIOD_OF_TIME = 0.001
PLOT_HEIGHT = 15
PLOT_WIDTH = 7.5
COLOUR_V0_X = 0
COLOUR_V0_Y = 0
COLOUR_A0 = 0

class ball:
    def __init__(self, pos_x, pos_y, v_x, v_y,a):
        self.x_0 = pos_x
        self.y_0 = pos_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x0 = v_x
        self.v_y0 = v_y
        self.v_x = v_x
        self.v_y = v_y
        self.a = a
        self.velocity()
        self.a_axis("x")
        self.a_axis("y")
        self.out = 0
        self.hit = 0
    
    def a_axis(self,axis):
        if axis == "x":
            if self.v == 0:
                self.a_x = 0
            else:
                self.a_x = self.a*self.v_x/self.v
        elif axis == "y":
            if self.v == 0:
                self.a_y = 0
            else:
                self.a_y = self.a*self.v_y/self.v
    
    def velocity(self):
        self.v = np.sqrt(np.float_power(self.v_x,2)+np.float_power(self.v_y,2))
        
    def x_t(self,t):
        self.pos_x = self.x_0 + self.v_x0 * t - self.a_x*t*t/2
        
    def y_t(self,t):
        self.pos_y = self.y_0 + self.v_y0 * t - self.a_y*t*t/2
        
    def final_velocity(self,t,s):
        direction = which_direction(self.v_x, self.v_y)
        if s == "x":
            self.v_x = fabs(fabs(self.v_x0) - fabs(self.a_x*t))
            if len(direction) == 2 and direction[1] == "W" or len(direction) == 1 and direction == "W":
                self.v_x *= -1
        elif s == "y":
            self.v_y = fabs(fabs(self.v_y0) - fabs(self.a_y*t))
            if len(direction) == 2 and direction[1] == "S" or len(direction) == 1 and direction == "S":
                self.v_y *= -1
            

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
        
        white_ball = ball(data_strings[0][0],data_strings[0][1],data_strings[1][0],data_strings[1][1],G*COF)
        colour_ball = ball(data_strings[2][0],data_strings[2][1],COLOUR_V0_X,COLOUR_V0_Y,COLOUR_A0)
        
        t_max = white_ball.v/white_ball.a
        t0 = 0 
        
        white_ball.move = 1
        colour_ball.move = 0
        
        global_hit = 0
        
        middle_white = [[],[]]
        middle_colour = [[],[]]
        white_crash = [[],[]]
        colour_crash = [[],[]]
        white_crash[0].append(white_ball.x_0)
        white_crash[1].append(white_ball.y_0)
        colour_crash[0].append(colour_ball.x_0)
        colour_crash[1].append(colour_ball.y_0)
        
        for t in np.arange (0,t_max,PERIOD_OF_TIME):
            if white_ball.move == 1:
                white_ball.x_t(t-t0)
                white_ball.y_t(t-t0)
                white_ball.final_velocity(t,"x")
                white_ball.final_velocity(t,"y")
                middle_white[0].append(white_ball.pos_x)
                middle_white[1].append(white_ball.pos_y)
            
            if colour_ball.move == 1:
                colour_ball.x_t(t-t0)
                colour_ball.y_t(t-t0)
                colour_ball.final_velocity(t,"x")
                colour_ball.final_velocity(t,"y")
                middle_colour[0].append(colour_ball.pos_x)
                middle_colour[1].append(colour_ball.pos_y)
            
            if is_in_hole(white_ball.pos_x,white_ball.pos_y,DIFFERENCE):
                white_ball.out = 1
                white_ball.move = 0
                
            if is_in_hole(colour_ball.pos_x,colour_ball.pos_y,DIFFERENCE):
                colour_ball.out = 1
                colour_ball.move = 0
                
            direction = []
            
            if does_hit_wall(colour_ball.pos_x,colour_ball.pos_y,DIFFERENCE,direction):
                t0 = t
                colour_ball.hit += 1
                colour_ball.x_0 = colour_ball.pos_x
                colour_ball.y_0 = colour_ball.pos_y
                colour_ball.v_x,colour_ball.v_y = energy_loss(colour_ball.v_x,colour_ball.v_y)
                if direction[0] == "N" or direction[0] == "S":
                    colour_ball.v_y *= -1
                    colour_ball.v_y0 *= -1
                    colour_ball.a_y *= -1
                elif direction[0] == "E" or direction[0] == "W":
                    colour_ball.v_x *= -1
                    colour_ball.v_x0 *= -1
                    colour_ball.a_x *= -1
                    
            direction = []        
                    
            if does_hit_wall(white_ball.pos_x,white_ball.pos_y,DIFFERENCE,direction):
                t0 = t
                white_ball.hit += 1
                white_ball.x_0 = white_ball.pos_x
                white_ball.y_0 = white_ball.pos_y
                white_ball.v_x,white_ball.v_y = energy_loss(white_ball.v_x,white_ball.v_y)
                if direction[0] == "N" or direction[0] == "S":
                    white_ball.v_y *= -1
                    white_ball.v_y0 *= -1
                    white_ball.a_y *= -1
                elif direction[0] == "E" or direction[0] == "W":
                    white_ball.v_x *= -1
                    white_ball.v_x0 *= -1
                    white_ball.a_x *= -1            
            
            if ball_hit(white_ball.pos_x,white_ball.pos_y,colour_ball.pos_x,colour_ball.pos_y, R):
                white_ball.v_x, colour_ball.v_x = colour_ball.v_x, white_ball.v_x
                white_ball.v_y, colour_ball.v_y = colour_ball.v_y, white_ball.v_y
                white_ball.v_x0, colour_ball.v_x0 = colour_ball.v_x0, white_ball.v_x0
                white_ball.v_y0, colour_ball.v_y0 = colour_ball.v_y0, white_ball.v_y0
                white_ball.move, colour_ball.move = colour_ball.move, white_ball.move
                white_ball.a_x, colour_ball.a_x = colour_ball.a_x, white_ball.a_x
                white_ball.a_y, colour_ball.a_y = colour_ball.a_y, white_ball.a_y
                
                white_crash[0].append(white_ball.pos_x)
                white_crash[1].append(white_ball.pos_y)
                colour_crash[0].append(colour_ball.pos_x)
                colour_crash[1].append(colour_ball.pos_y)
                
                t0 = t
                global_hit += 1
        
        white_crash[0].append(white_ball.pos_x)
        white_crash[1].append(white_ball.pos_y)
        colour_crash[0].append(colour_ball.pos_x)
        colour_crash[1].append(colour_ball.pos_y)
        
        x_table_1 = [i for i in np.arange(D/2,(TABLE_WIDTH-D)/2+DENSITY,DENSITY)]
        x_table_2 = [i for i in np.arange((TABLE_WIDTH+D)/2,TABLE_WIDTH-D/2+DENSITY,DENSITY)]
        y_table_1 = [i for i in np.arange(D/2,TABLE_HEIGHT-D/2+DENSITY,DENSITY)]
        y_table_2 = []
        x_table_3 = []
        x_table_4 = []
        y_table_3 = []
        
        for j in range(len(x_table_1)):
            y_table_2.append(0)
            y_table_3.append(TABLE_HEIGHT)
            
        for j in range(len(y_table_1)):
            x_table_3.append(0)
            x_table_4.append(TABLE_WIDTH)
        
        plt.figure(figsize=(PLOT_HEIGHT,PLOT_WIDTH))
        plt.title("Trajectory no. " + str(i+1))
        plt.axis('off')
        plt.plot(x_table_1,y_table_2,color="black")
        plt.plot(x_table_1,y_table_3,color="black")
        plt.plot(x_table_2,y_table_2,color="black")
        plt.plot(x_table_2,y_table_3,color="black")
        plt.plot(x_table_3,y_table_1,color="black")
        plt.plot(x_table_4,y_table_1,color="black")
        plt.plot(middle_white[0],middle_white[1],'r--',color="red")
        plt.plot(middle_colour[0],middle_colour[1],'r--',color='blue')
        plt.plot(white_crash[0],white_crash[1],'ro',color="red")
        plt.plot(colour_crash[0],colour_crash[1],'ro',color='blue')
        
        if white_ball.out:
            output_line += "(foul); "
        else:
            output_line += "(" + str(round(white_ball.pos_x,2)) + ", " + str(round(white_ball.pos_y,2)) + "); "
        
        if colour_ball.out:
            output_line += "(score); "
        else:
            output_line += "(" + str(round(colour_ball.pos_x,2)) + ", " + str(round(colour_ball.pos_y,2)) + "); "
        
        output_line += str(global_hit) + "; " + str(white_ball.hit) + "; " + str(colour_ball.hit)
        output_strings.append(output_line)
        
        plt.savefig(str(i+1)+".png")
    
    np.savetxt("output.txt", output_strings,fmt="%s")
               
def ball_hit(x1,y1,x2,y2,r):
    if np.sqrt(np.float_power(x2-x1,2)+np.float_power(y2-y1,2)) <= 2*r:
        return 1
    return 0

def energy_loss(v_x,v_y):
    return v_x*np.sqrt(ENERGY_LEFT),v_y*np.sqrt(ENERGY_LEFT)

def is_in_hole(x,y,dif):
    if ((fabs(x-TABLE_WIDTH) <= dif or fabs(x) <= dif) and ((y >= 0 and y <= D/2) or (y <= TABLE_HEIGHT and y >= TABLE_HEIGHT-D/2))):
        return 1
    elif ((fabs(y) <= dif or fabs(y-TABLE_HEIGHT) <= dif) and ((x >= 0 and x <= D/2) or (x >= (TABLE_WIDTH-D)/2 and x <= (TABLE_WIDTH+D)/2) or (x >= TABLE_WIDTH-D/2 and x <= TABLE_WIDTH))):
        return 1
    return 0

def does_hit_wall(x,y,dif,d):
    if ((fabs(x-TABLE_WIDTH) <= dif) and ((y >= D/2 and y <= TABLE_HEIGHT-D/2))): #eastern wall
        d.append("E")
        return 1
    elif ((fabs(x) <= dif) and ((y >= D/2 and y <= TABLE_HEIGHT-D/2))):           #western wall
        d.append("W")
        return 1
    elif ((fabs(y) <= dif) and ((x >= D/2 and x <= (TABLE_WIDTH-D)/2) or (x >= (TABLE_WIDTH+D)/2 and x <= TABLE_WIDTH-D/2))):       #southern wall
        d.append("S")
        return 1
    elif ((fabs(y-TABLE_HEIGHT) <= dif) and ((x >= D/2 and x <= (TABLE_WIDTH-D)/2) or (x >= (TABLE_WIDTH+D)/2 and x <= TABLE_WIDTH-D/2))):       #northern wall
        d.append("N")
        return 1
    return 0

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
        for j in range (len(array[i])):
            array[i][j] = float(array[i][j])
        
main()
