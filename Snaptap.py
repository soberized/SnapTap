import keyboard
import threading
import time

a_held = d_held = w_held = s_held = 0
a_scrip = d_scrip = w_scrip = s_scrip = 0

def handle_a(e):
    global a_held, d_held, a_scrip, d_scrip
    if e.event_type == keyboard.KEY_DOWN:
        a_held = 1
        if d_scrip:
            d_scrip = 0
            keyboard.release('d')
        a_scrip = 1
        keyboard.press('a')
    else:
        a_held = 0
        if a_scrip:
            a_scrip = 0
            keyboard.release('a')
        if d_held and not d_scrip:
            d_scrip = 1
            keyboard.press('d')

def handle_d(e):
    global a_held, d_held, a_scrip, d_scrip
    if e.event_type == keyboard.KEY_DOWN:
        d_held = 1
        if a_scrip:
            a_scrip = 0
            keyboard.release('a')
        d_scrip = 1
        keyboard.press('d')
    else:
        d_held = 0
        if d_scrip:
            d_scrip = 0
            keyboard.release('d')
        if a_held and not a_scrip:
            a_scrip = 1
            keyboard.press('a')

def handle_w(e):
    global w_held, s_held, w_scrip, s_scrip
    if e.event_type == keyboard.KEY_DOWN:
        w_held = 1
        if s_scrip:
            s_scrip = 0
            keyboard.release('s')
        w_scrip = 1
        keyboard.press('w')
    else:
        w_held = 0
        if w_scrip:
            w_scrip = 0
            keyboard.release('w')
        if s_held and not s_scrip:
            s_scrip = 1
            keyboard.press('s')

def handle_s(e):
    global w_held, s_held, w_scrip, s_scrip
    if e.event_type == keyboard.KEY_DOWN:
        s_held = 1
        if w_scrip:
            w_scrip = 0
            keyboard.release('w')
        s_scrip = 1
        keyboard.press('s')
    else:
        s_held = 0
        if s_scrip:
            s_scrip = 0
            keyboard.release('s')
        if w_held and not w_scrip:
            w_scrip = 1
            keyboard.press('w')

def press_s_briefly():
    keyboard.press('s')
    time.sleep(0.2)
    keyboard.release('s')

def handle_a_fivem(e):
    global a_held, d_held, a_scrip, d_scrip
    if e.event_type == keyboard.KEY_DOWN:
        if not a_held:
            a_held = 1
            if d_scrip:
                d_scrip = 0
                keyboard.release('d')
                threading.Thread(target=press_s_briefly).start()
            a_scrip = 1
            keyboard.press('a')
    else:
        a_held = 0
        if a_scrip:
            a_scrip = 0
            keyboard.release('a')
        if d_held and not d_scrip:
            d_scrip = 1
            keyboard.press('d')
            threading.Thread(target=press_s_briefly).start()

def handle_d_fivem(e):
    global a_held, d_held, a_scrip, d_scrip
    if e.event_type == keyboard.KEY_DOWN:
        if not d_held:
            d_held = 1
            if a_scrip:
                a_scrip = 0
                keyboard.release('a')
                threading.Thread(target=press_s_briefly).start()
            d_scrip = 1
            keyboard.press('d')
    else:
        d_held = 0
        if d_scrip:
            d_scrip = 0
            keyboard.release('d')
        if a_held and not a_scrip:
            a_scrip = 1
            keyboard.press('a')
            threading.Thread(target=press_s_briefly).start()

mode_as = True
mode_ws = False
mode_fivem = False

if mode_as:
    keyboard.on_press_key('a', handle_a, suppress=True)
    keyboard.on_release_key('a', handle_a, suppress=True)
    keyboard.on_press_key('d', handle_d, suppress=True)
    keyboard.on_release_key('d', handle_d, suppress=True)
elif mode_ws:
    keyboard.on_press_key('w', handle_w, suppress=True)
    keyboard.on_release_key('w', handle_w, suppress=True)
    keyboard.on_press_key('s', handle_s, suppress=True)
    keyboard.on_release_key('s', handle_s, suppress=True)
elif mode_fivem:
    keyboard.on_press_key('a', handle_a_fivem, suppress=True)
    keyboard.on_release_key('a', handle_a_fivem, suppress=True)
    keyboard.on_press_key('d', handle_d_fivem, suppress=True)
    keyboard.on_release_key('d', handle_d_fivem, suppress=True)

print("Script is running. Press Ctrl+C to exit.")
keyboard.wait('esc')