from main_screen import main_screen

try:
    from tkinter import filedialog
    from tkinter import messagebox
    import tkinter.font
    import tkinter as tk
except:
    import Tkinter as tk
    import Tkinter.font
    from tkinter import filedialog
    from tkinter import messagebox

class start_screen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None

        self.title("Word frequency checker")
        #self.resizable(False,False)
        self.resizable(True,True)
        self.switch_frame(main_screen)

    # 매개변수 message는 다음 단계로 넘어갈 때 조건 값을 넣지 않으면 경고창이 뜰 수 있게 만드는 매개 변수
    def switch_frame(self, frame_class, message="  "):
        new_frame = frame_class(self)
        if message == " ":
            tk.messagebox.showwarning("원하는 조건을 체크해주세요.")
        if message == -1:
            tk.messagebox.showwarning("조건에 해당되는 범위를 입력하고 확인버튼을 눌러주세요.")

        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

