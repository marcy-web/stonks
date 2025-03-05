import curses
import time

def news_ticker(stdscr, text, speed=0.1, bg_color=1, text_color=0):
    """
    Create a simple news ticker that scrolls text from right to left
    
    Args:
        stdscr: curses window object
        text: text to scroll
        speed: delay between updates (lower = faster)
        bg_color: background color pair number
        text_color: text color pair number
    """
    # Clear screen and hide cursor
    stdscr.clear()
    curses.curs_set(0)
    
    # Initialize color pairs if the terminal supports colors
    if curses.has_colors():
        curses.start_color()
        
        # Create color pairs
        # 1: White text on Blue background (default ticker)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        # 2: Yellow text on Red background (breaking news)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)
        # 3: Black text on Green background (financial news)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
        # 4: White text on Magenta background (entertainment)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    
    # Get screen dimensions
    height, width = stdscr.getmaxyx()
    
    # Prepare text by adding padding
    padded_text = " " * width + text + " " * width
    
    # Set up initial position
    position = 0
    
    # Fill the entire background with the specified color
    for y in range(height):
        stdscr.addstr(y, 0, " " * (width-1), curses.color_pair(bg_color))
    
    # Start scrolling
    try:
        while True:
            # Calculate the portion of text to display
            display_text = padded_text[position:position+width]
            
            # Fill the ticker line with background color first
            ticker_row = height//2
            stdscr.addstr(ticker_row, 0, " " * (width-1), curses.color_pair(bg_color))
            
            # Display the text in the middle of the screen with specified color
            stdscr.addstr(ticker_row, 0, display_text, curses.color_pair(bg_color))
            
            # Refresh the screen
            stdscr.refresh()
            
            # Move to the next position
            position += 1
            
            # Reset position if we've gone through the whole text
            if position >= len(padded_text) - width:
                position = 0
            
            # Pause before the next update
            time.sleep(speed)
    except KeyboardInterrupt:
        # Exit gracefully on Ctrl+C
        pass

# Example usage
if __name__ == "__main__":
    # News headlines for the ticker
    news_text = "BREAKING NEWS: Python found to be most readable programming language * WEATHER: It's sunny in Pythonville * TECH: New curses library update improves performance * SPORTS: Snake charmers win championship"
    
    # Initialize and run with curses
    # You can choose different color pairs:
    # 1: White on Blue (default)
    # 2: Yellow on Red (breaking news style)
    # 3: Black on Green (financial news style)
    # 4: White on Magenta (entertainment style)
    curses.wrapper(lambda stdscr: news_ticker(stdscr, news_text, 0.05, bg_color=2))