import subprocess
import sys
import time
import os
import shutil
from subprocess import Popen, PIPE

# == FlyFF server launcher by SquonK, 2019-2020 ==
# The intent of this program is to fluidify the workflow by having an easy way
# to update server executable for local testing purposes.
#
# Error checking is kept to a minimum as this program is not intended to be use in production context

# Options
# GIT_EXECUTABLE_PATH = None  # If you want the git button, replace with the path a git executable
GIT_EXECUTABLE_PATH = "C:\\Program Files\\Git\\git-bash.exe"


# Represents a generic program with a source file where is written the compiled program and a destination executable.
class Program:
    def __init__(self, executable, source):
        self.executable = executable
        self.source = source
        self.dateofexecutable = os.path.getmtime(self.executable)
        self.isuptodate = True
        self.functions = []
    
    def kill_all_process(self):
        print("Abstract method : Not implemented")
    
    # Returns true if the stored executable is up to date according to the source
    def is_up_to_date(self):
        if not self.isuptodate:
            return False
        
        timestampofstored = None
        
        try:
            timestampofstored = os.path.getmtime(self.source)
        except FileNotFoundError:
            return True
            
        self.isuptodate = self.dateofexecutable >= timestampofstored
        
        return self.isuptodate
    
    # If needed, update the program. Kills the process if running. Returns true if the program has been updated
    def update(self):
        if self.is_up_to_date():
            return False
        
        self.kill_all_process()
        
        shutil.copy2(self.source, self.executable)
        self.dateofexecutable = os.path.getmtime(self.executable)
        self.isuptodate = True
        
        return True
    
    def start_a_new_process(self, startupinfo):
        return subprocess.Popen(self.executable, -1, startupinfo=startupinfo, cwd=self.cwd)
    
    # == Communication with GUI ==
    def bind(self, function):
        self.functions.append(function)
        
    def use_bind(self):
        for function in self.functions:
            function(self)
    
# Represents the client, which is 1 program and 0-n process
class ProgramClient(Program):
    def __init__(self, executable, source):
        Program.__init__(self, executable, source)
        self.processes = []
        self.cwd = "..\\Resource\\"
        
    def kill_all_process(self):
        for process in self.processes:
            process.kill()
            
        while self.get_number_of_processes() != 0:
            time.sleep(0.1)
        
    def start_new_process(self):
        if self.get_number_of_processes() == 0:
            self.update()
    
        self.processes.append(self.start_a_new_process(None))
    
    def get_number_of_processes(self):
        self.processes = [p for p in self.processes if p.poll() is None]
    
        return len(self.processes)
        
    # Start a new process. If not up to date, kill every process to update the file
    def start_updated(self):
        self.kill_all_process()
        self.start_new_process()
        
    def open_ini(self):
        ini_file = self.executable[:-3] + "ini"
        os.startfile(ini_file)


# Represents the server, which is 1 program and 0-1 process
class ProgramServer(Program):
    startuphidden = None

    @staticmethod
    def ensure_startup_exist():
        if ProgramServer.startuphidden is None:
            if os.name == 'nt':
                ProgramServer.startuphidden = subprocess.STARTUPINFO()
                ProgramServer.startuphidden.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    # Initialize the program
    def __init__(self, executable, source, hide=True):
        Program.__init__(self, "..\\Program\\" + executable, source)
    
        # Passed properties
        self.hide = hide
        self.check_box = None
        self.cwd = None
        
        ProgramServer.ensure_startup_exist()
        
        # Built properties
        self.process = None
        self.cwd = "..\\Program\\"
                
    # Returns true if a process for this program is running
    def is_running(self):
        if self.process is None:
            return False
        
        if self.process.poll() is None:
            return True
            
        self.process = None
        return False
        
    # If the process is running, kills it
    def kill_all_process(self):
        if self.process is None:
            return
        
        self.process.kill()
        self.process = None
            
    def get_status(self):
        if not self.is_running():
            return FlyFFLauncher.STATUS_OFF
        elif self.is_up_to_date():
            return FlyFFLauncher.STATUS_STARTED
        else:
            return FlyFFLauncher.STATUS_OBSOLETE
    
    def start(self):
        restart = False
        
        if not self.is_up_to_date():
            self.update()
            restart = True
        
        if self.is_running() and not restart:
            return FlyFFLauncher.ALREADY_STARTED
        
        startupinfo = ProgramServer.startuphidden if self.hide else None
        
        self.process = self.start_a_new_process(startupinfo)
        
        time.sleep(1)

        if self.is_running():
            return FlyFFLauncher.CHANGED_PROCESS
        else:
            return FlyFFLauncher.COULDNT_START
            

# Global launcher
class FlyFFLauncher:
    # Constants
    CHANGED_PROCESS = 0
    COULDNT_START = 1
    ALREADY_STARTED = 2
    STATUS_STARTED = 3
    STATUS_OFF = 4
    STATUS_OBSOLETE = 5
    
    # Constructor
    def __init__(self):
        self.client = ProgramClient('..\\Resource\\Neuz.exe', '..\\Output\\Neuz\\NoGameguard\\Neuz.exe')
        self.server = ProgramServer('WorldServer.exe', '..\\Output\\{0}\\Release\\{0}.exe'.format('WorldServer'), False)
    
    # Launch every process of the list
    def start(self):
        error = self.server.start() 
        if error == FlyFFLauncher.COULDNT_START:
            return False
        return True
    
    def kill_server(self):
        self.server.kill_all_process()
    
    def kill(self):
        self.server.kill_all_process()
        self.client.kill_all_process()
        
    def open_dir(self):
        os.startfile("..\\")
    
    # GUI
    def bind_server(self, function):
        self.server.bind(function)
        
    def bind_client(self, function):
        self.client.bind(function)
        
    def apply_server(self, function):
        function(self.server)
        
    def apply_client(self, function):
        function(self.client)
        
    def use_binds(self):
        self.server.use_bind()
        self.client.use_bind()


# ==== LINK WITH UI ====

def link_with_gui(root, interface):
    # Import tkinter
    try:
        import Tkinter as tk
    except ImportError:
        import tkinter as tk

    # Master model object
    flyff = FlyFFLauncher()
    
    # On close
    import atexit

    def onClose():
        flyff.kill()

    atexit.register(onClose)
    
    # Extra button
    interface.OpenFlyFFDir.configure(command=flyff.open_dir)
    
    # Bindings    
    status_color = {
        FlyFFLauncher.STATUS_STARTED: "#005000",
        FlyFFLauncher.STATUS_OFF: "#FF0000",
        FlyFFLauncher.STATUS_OBSOLETE: "#FF8000"
    }
    
    # Server Bindings
    def install_server_bindings():
        status_text = {
            FlyFFLauncher.STATUS_STARTED: "Server is running",
            FlyFFLauncher.STATUS_OFF: "Server is off",
            FlyFFLauncher.STATUS_OBSOLETE: "Server can be updated"
        }

        check_box = interface.ServCbx01
        def copy_name(program):
            if program.hide:
                state = tk.NORMAL
                check_box.deselect()
            else:
                state = tk.ACTIVE
                check_box.select()
            
            def change():
                program.hide = not program.hide
            
            check_box.configure(state=state)
            check_box.configure(command=change)
            program.check_box = check_box
        
        def write_status(program):
            interface.ServState01.configure(text=status_text.get(program.get_status(), "Unknown"))
            interface.ServState01.configure(foreground=status_color.get(program.get_status(), "black"))
    
        flyff.apply_server(copy_name)
        flyff.bind_server(write_status)
    
    install_server_bindings()

    def start_in_new_thread():
        from threading import Thread
        
        class StartingThread(Thread):
            def __init__(self):
                Thread.__init__(self)
    
            def run(self):
                button_list = [interface.ServStart_2, interface.ServStart_1]
                for b in button_list:
                    b.configure(state=tk.DISABLED)
                flyff.start()
                for b in button_list:
                    b.configure(state=tk.NORMAL)
    
        thread = StartingThread()
        thread.start()
    
    interface.ServStart_1.configure(command=start_in_new_thread)
    interface.ServStart_2.configure(command=flyff.kill_server)
    
    
    # Client
    def to_bind_client(client):
        if client.is_up_to_date():
            text = "Neuz is up to date"
            color = status_color.get(FlyFFLauncher.STATUS_STARTED)
        else:
            text = "Neuz can be updated"
            color = status_color.get(FlyFFLauncher.STATUS_OBSOLETE)
        
        interface.ClientState.configure(text=text)
        interface.ClientState.configure(foreground=color)
        
        started_neuz = flyff.client.get_number_of_processes()
        
        if started_neuz == 0:
            text = "No neuz running"
            color = status_color.get(FlyFFLauncher.STATUS_OFF)
        else:
            text = str(started_neuz) + " neuz running"
            color = status_color.get(FlyFFLauncher.STATUS_STARTED)
        
        interface.ClientState2.configure(text=text)
        interface.ClientState2.configure(foreground=color)
    
    flyff.bind_client(to_bind_client)
    
    interface.ClientStartBig.configure(command=flyff.client.start_new_process)
    interface.ClientUpdate.configure(text='''Restart One''')
    interface.ClientUpdate.configure(command=flyff.client.start_updated)
    interface.ClientKill.configure(command=flyff.client.kill_all_process)
    interface.ClientIni.configure(command=flyff.client.open_ini)
    
    # Git Button
    if GIT_EXECUTABLE_PATH is None:
        interface.GitButton.place_forget()
    else:
        def git_opener():
            subprocess.Popen(GIT_EXECUTABLE_PATH, cwd="..")
        interface.GitButton.configure(command=git_opener)
    
    # Apply binds
    def perpetual():
        flyff.use_binds()
        root.after(1000, perpetual)
        
    perpetual()
