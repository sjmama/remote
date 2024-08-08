import mouse
import keyboard
import time
import threading

scroll_start_time=0

# 상태 저장 변수
stat = {
    "mpos": (0, 0),
    "mbutton": set(),
    "click": False,
    "scroll": 0,
    "keys": set()
}

def on_move(event):
    stat["mpos"] = (event.x, event.y)

def on_click(event):
    print(event)
    if event.event_type == 'down' or event.event_type == 'double':
        stat["mbutton"].add(event.button)
        stat['click']=True
    else:
        stat["mbutton"].discard(event.button)
        if len(stat["mbutton"]) == 0:
            stat["click"]=False
            
def on_scroll(event):
    global scroll_start_time
    scroll_start_time = event.time
    stat["scroll"] = event.delta

def scroll_checker():
    while True:
        if time.time() - scroll_start_time > 0.2:
            stat['scroll'] = 0 
        time.sleep(0.01)  # 0.1초마다 체크
        
mevent = {
    "MoveEvent":on_move,
    "WheelEvent":on_scroll,
    "ButtonEvent":on_click
}

def on_mouse_event(event):
    event_type = type(event).__name__
    mevent[event_type](event)
    
# 마우스 이벤트 핸들러


# 키보드 이벤트 핸들러
def on_key_event(event):
    #print(event.to_json() )
    if event.event_type == "down":
        stat["keys"].add(event.scan_code)
    elif event.event_type == "up":
        stat["keys"].discard(event.scan_code)


# 상태 출력 함수
def print_stat():
    while True:
        print(stat)
        stat["scroll"] = 0  # 스크롤 상태 초기화
        time.sleep(0.1)    

def tat():
    return stat

def main():
    scroll_checker_thread = threading.Thread(target=scroll_checker)
    scroll_checker_thread.daemon = True  # 메인 스레드가 종료되면 종료
    scroll_checker_thread.start()
    # 마우스 이벤트 리스너 등록
    mouse.hook(on_mouse_event)
    # 키보드 이벤트 리스너 등록
    keyboard.hook(on_key_event)
    # 상태 출력 스레드 시작
    thread = threading.Thread(target=print_stat)
    thread.daemon = True
    thread.start()
main()
# 메인 스레드는 대기
keyboard.wait('esc')  # 'esc' 키를 누르면 프로그램 종료