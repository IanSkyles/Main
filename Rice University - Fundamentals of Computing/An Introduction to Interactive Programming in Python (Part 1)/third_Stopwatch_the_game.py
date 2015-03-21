# Ian Skyles
# Mini Project 3: Stopwatch: The Game
# March 20th, 2015 (3/20/2015)
# An Introduction to Interactive Programming in Python (Part 1)

#imports
import simplegui

# define global variables
timer_interval = 100 #100ms interval
time = 0 # 1 = 1ms, 10 = 1s
total_timer_stops = 0
total_stops_on_target = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #formats the time (in milliseconds) into a minutes:seconds:milliseconds
    minutes = t / 600
    seconds_first_digit = ((t/10) % 60)/10
    seconds_second_digit = (t / 10) % 10
    seconds = str(seconds_first_digit) + str(seconds_second_digit)    
    milli_seconds = t % 10
    return str(minutes) + ":" + str(seconds) + ":" + str(milli_seconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    #starts the timer
    timer.start()

def stop_button_handler():
    global total_timer_stops
    global total_stops_on_target
    global time
    if(timer.is_running()):        
        total_timer_stops += 1
        if((time % 10) == 0):
            total_stops_on_target += 1
    #stops the timer
    timer.stop()

def reset_button_handler():
    #resets the time
    global time
    global total_timer_stops
    global total_stops_on_target
    time = 0
    total_timer_stops = 0
    total_stops_on_target = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [50, 100], 36, "Red")
    canvas.draw_text(str(total_stops_on_target) + "/" + str(total_timer_stops)
                    , [150,25], 25, "Blue")
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 200)

# create timer and register event handlers
timer = simplegui.create_timer(timer_interval, timer_handler)
frame.set_draw_handler(draw)
#add buttons
frame.add_button("Start", start_button_handler)
frame.add_button("Stop", stop_button_handler)
frame.add_button("Reset", reset_button_handler)
# start frame
frame.start()
