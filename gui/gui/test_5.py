from threading import Thread

import pyautogui

import win32api

import time



class AutoReadManga:

    def __init__(self):

        self.canScroll = False

        self.AltL = True

        self.AltK = False



    def Start(self):

        self.canScroll = True

        while self.canScroll == True:

            pyautogui.scroll(-10)



    def Stop(self):

        self.canScroll = False



    def Run(self):

        while True:

            if self.AltL:

                if win32api.GetAsyncKeyState(164) and win32api.GetAsyncKeyState(76):

                    Thread(target=self.Start).start()

                    self.AltL = False

                    self.AltK = True

            if self.AltK:

                if win32api.GetAsyncKeyState(164) and win32api.GetAsyncKeyState(75):

                    self.Stop()

                    self.AltL = True

                    self.AltK = False

            elif win32api.GetAsyncKeyState(164) and win32api.GetAsyncKeyState(81):

                quit()

            time.sleep(0.01)



LuckyEgg = AutoReadManga()

LuckyEgg.Run()