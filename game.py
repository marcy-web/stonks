import numpy
import asciichartpy
import shutil
import textwrap
import time

numpy.set_printoptions(suppress=True, precision=1, floatmode='fixed')

def main():
    try:
        terminal_width = shutil.get_terminal_size().columns
        terminal_height = shutil.get_terminal_size().lines
        chart_width = terminal_width - 10
        chart_height = terminal_height - 10
        
        # variable declarations
        time_steps = min(100, chart_width)  # make sure it's not wider than the terminal
        number_of_paths = 1
        time_horizon = 1.0
        
        # generate da path
        time_points = numpy.linspace(0.0, time_horizon, time_steps)
        time_differential = time_points[1] - time_points[0]
        brownian_differential = numpy.sqrt(time_differential) * numpy.random.normal(size=(time_steps - 1, number_of_paths))
        brownian_start = numpy.zeros(shape=(1, number_of_paths))
        brownian_paths = numpy.concatenate((brownian_start, numpy.cumsum(brownian_differential, axis=0)), axis=0)
        
        complete_path = brownian_paths.flatten().tolist()
        
        # animation stuff
        total_animation_time = 30  # trading day length in seconds
        update_interval = total_animation_time / time_steps
        
        for i in range(time_steps): 
            print("\033c", end="")
            
            current_path = complete_path[:i+1]
            
            #draw chart
            chart = asciichartpy.plot(current_path, {
                'height': chart_height,
                'width': chart_width,
                'colors': [asciichartpy.green if current_path[-1] >= 0 else asciichartpy.red]
            })
            
            print(chart)
            
            current_price = current_path[-1]
            price_change = current_price - current_path[-2] if i > 0 else 0
            print(f"Current Price: ${current_price:.2f}  ({'+' if price_change >= 0 else ''}{price_change:.2f})")
            
            time.sleep(update_interval)
    except KeyboardInterrupt:
        print("\nProgram stopped")

main()