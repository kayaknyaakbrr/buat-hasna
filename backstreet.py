import sys
import time

def lirik_aesthetic():
    colors = {
        'reset': '\033[0m',
        'cyan': '\033[96m',
        'magenta': '\033[95m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'green': '\033[92m'
    }
    color_cycle = [colors['cyan'], colors['magenta'], colors['blue'], colors['yellow'], colors['green']]
    
    lines = [
        ("I'm lookin' back on things I've done", 0.08 ),
        ("I never wanna play the same old part", 0.08),
        ("Keep you in the dark (keep you in the dark)", 0.08),
        ("Now let me show you the shape of my heart", 0.09),
        ("Looking back on the things I've done", 0.08),
        ("I was trying to be someone (trying to be someone)", 0.08),
        ("Played my part, kept you in the dark", 0.12),
        ("Now let me show you the shape of my heart", 0.15),
    ]

    print("\n--- Playing: Shape of My Heart ---\n")
    time.sleep(1) 
    for i, (text, char_delay) in enumerate(lines):
        color = color_cycle[i % len(color_cycle)]
        print(color, end='')
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        print(colors['reset']) 

if __name__ == "__main__":
    lirik_aesthetic()