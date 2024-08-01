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

def on_stat():
    while True:
        keyboard.send((stat["keys"]))
        mouse.move(stat["keys"])
        time.sleep(0.1)

# 상태 출력 스레드 시작
thread = threading.Thread(target=on_stat)
thread.daemon = True
thread.start()

# 메인 스레드는 대기
keyboard.wait('esc')  # 'esc' 키를 누르면 프로그램 종료