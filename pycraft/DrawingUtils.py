if __name__ != "__main__":
    print("Started <Pycraft_DrawingUtils>")

    class DrawRose:
        def __init__(self):
            pass

        def CreateRose(self, xScaleFact, yScaleFact, coloursARRAY):
            try:
                if coloursARRAY is False:
                    coloursARRAY = []
                    for i in range(32):
                        coloursARRAY.append(self.ShapeCol)

                defLargeOctagon = [(205*xScaleFact, 142*yScaleFact),
                                   (51*xScaleFact, 295*yScaleFact),
                                   (51*xScaleFact, 512*yScaleFact),
                                   (205*xScaleFact, 666*yScaleFact),
                                   (422*xScaleFact, 666*yScaleFact),
                                   (575*xScaleFact, 512*yScaleFact),
                                   (575*xScaleFact, 295*yScaleFact),
                                   (422*xScaleFact, 142*yScaleFact)]

                self.mod_Pygame__.draw.polygon(
                    self.Display,
                    self.ShapeCol,
                    defLargeOctagon,
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[0],
                    (205*xScaleFact,142*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[1],
                    (205*xScaleFact, 142*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[2],
                    (205*xScaleFact, 142*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[3],
                    (205*xScaleFact, 142*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[4],
                    (205*xScaleFact, 142*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[5],
                    (51*xScaleFact, 295*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[6],
                    (51*xScaleFact, 295*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[7],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[8],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[9],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[10],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[11],
                    (51*xScaleFact, 512*yScaleFact),
                    (51*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[12],
                    (51*xScaleFact, 512*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[13],
                    (51*xScaleFact, 512*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[14],
                    (51*xScaleFact, 512*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[15],
                    (51*xScaleFact, 512*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[16],
                    (51*xScaleFact, 512*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[17],
                    (205*xScaleFact, 666*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[18],
                    (205*xScaleFact, 666*yScaleFact),
                    (51*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[19],
                    (205*xScaleFact, 666*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[20],
                    (205*xScaleFact, 666*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[21],
                    (205*xScaleFact, 666*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[22],
                    (205*xScaleFact, 666*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[23],
                    (51*xScaleFact, 295*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[24],
                    (51*xScaleFact, 295*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[25],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[25],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[27],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[28],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[29],
                    (422*xScaleFact, 666*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[30],
                    (422*xScaleFact, 666*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_Pygame__.draw.line(
                    self.Display,
                    coloursARRAY[31],
                    (575*xScaleFact, 512*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

            except Exception as Message:
                self.ErrorMessage = "DrawingUtils > DrawRose > CreateRose: "+str(Message)

                self.ErrorMessage_detailed = "".join(
                    self.mod_Traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(self)

    class GenerateGraph:
        def __init__(self):
            pass

        def CreateDevmodeGraph(self, DataFont):
            if self.Devmode == 10:
                try:
                    if ((self.realWidth/2)+100)+self.Timer >= self.realWidth:
                        self.Data_aFPS = []
                        self.Data_CPUUsE = []
                        self.Data_eFPS = []
                        self.Data_MemUsE = []

                        self.Timer = 0

                        self.Data_aFPS_Max = 1
                        self.Data_CPUUsE_Max = 1
                        self.Data_eFPS_Max = 1
                        self.Data_MemUsE_Max = 50
                        self.Data_CPUUsE_Max = 50

                    BackingRect = self.mod_Pygame__.Rect(
                        (self.realWidth/2)+100,
                        0,
                        self.realWidth,
                        200)

                    self.mod_Pygame__.draw.rect(
                        self.Display,
                        self.ShapeCol,
                        BackingRect)

                    SwapMemory = self.mod_Psutil__.swap_memory()
                    VirtualMemory = self.mod_Psutil__.virtual_memory()

                    TotalMemory = SwapMemory.total+VirtualMemory.total
                    UsedMemory = SwapMemory.used+VirtualMemory.used

                    self.CurrentMemoryUsage = (100/TotalMemory)*(UsedMemory)

                    if self.Timer >= 2:
                        self.Data_aFPS.append(
                            [((self.realWidth/2)+100)+self.Timer,
                             200-(100/self.Data_aFPS_Max)*(self.aFPS/(self.Iteration))])

                        try:
                            self.Data_eFPS.append(
                                [((self.realWidth/2)+100)+self.Timer,
                                 200-(100/self.Data_eFPS_Max)*int(self.eFPS)])

                        except:
                            self.Data_eFPS.append(
                                [((self.realWidth/2)+100)+self.Timer,
                                 200-(100/self.Data_eFPS_Max)*int(2000)])

                        self.Data_MemUsE.append(
                            [((self.realWidth/2)+100)+self.Timer,
                             200-(2)*self.CurrentMemoryUsage])

                    if self.FPS_Overclock:
                        self.Data_aFPS_Max = 2000
                    elif (self.aFPS/(self.Iteration)) > self.Data_aFPS_Max:
                        self.Data_aFPS_Max = (self.aFPS/(self.Iteration))

                    if self.eFPS > self.Data_eFPS_Max:
                        self.Data_eFPS_Max = self.eFPS

                    if self.CurrentMemoryUsage > self.Data_MemUsE_Max:
                        self.Data_MemUsE_Max = self.CurrentMemoryUsage

                    self.Timer += 0.2
                    if self.Timer >= 5:
                        self.mod_Pygame__.draw.lines(
                            self.Display,
                            (255, 0, 0),
                            False,
                            self.Data_aFPS)

                        self.mod_Pygame__.draw.lines(
                            self.Display,
                            (0, 255, 0),
                            False,
                            self.Data_eFPS)

                        self.mod_Pygame__.draw.lines(
                            self.Display,
                            (0, 0, 255),
                            False,
                            self.Data_MemUsE)

                    if len(self.Data_CPUUsE) >= 2:
                        self.mod_Pygame__.draw.lines(
                            self.Display,
                            (255, 0, 255),
                            False,
                            self.Data_CPUUsE)

                    if self.FPS_Overclock:
                        try:
                            runFont = DataFont.render(
                                "".join((f"MemUsE: {int(self.CurrentMemoryUsage)}% | ",
                                         f"CPUUsE: {self.mod_Psutil__.cpu_percent()}% | ",
                                         f"FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: ",
                                         f"N/A Iteration: {self.Iteration}")),
                                self.aa,
                                (255, 255, 255))

                        except:
                            runFont = DataFont.render(
                                "".join((f"MemUsE: {int(self.CurrentMemoryUsage)}% | ",
                                         f"CPUUsE: {self.mod_Psutil__.cpu_percent()}% | ",
                                         f"FPS: {self.FPS} eFPS: NaN* aFPS: ",
                                         f"N/A Iteration: {self.Iteration}")),
                                self.aa,
                                (255, 255, 255))
                    else:
                        runFont = DataFont.render(
                            "".join((f"MemUsE: {int(self.CurrentMemoryUsage)}% | ",
                                     f"CPUUsE: {self.mod_Psutil__.cpu_percent()}% | ",
                                     f"FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: ",
                                     f"{int(self.aFPS/self.Iteration)} ",
                                     f"Iteration: {self.Iteration}")),
                            self.aa,
                            (255, 255, 255))

                    self.Display.blit(
                        runFont,
                        ((self.realWidth/2)+105, 0))

                except Exception as Message:
                    self.ErrorMessage = "".join(("DrawingUtils > GenerateGraph ",
                                                 f"> CreateDevmodeGraph: {str(Message)}"))
                    self.ErrorMessage_detailed = "".join(
                        self.mod_Traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(self)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
