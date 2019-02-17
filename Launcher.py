import subprocess
import sys
import time
import os
import shutil
from subprocess import Popen, PIPE

# == FlyFF server launcher by SquonK, 2019 ==
# The intent of this program is to fluidify the workflow by having an easy way to update servers executable
# for local testing purposes.
#
# Error checking is kept to a minimum as this program is not intended to be use in production context


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
    
    
class ProgramClient(Program):
    def __init__(self, executable, source):
        Program.__init__(self, executable, source)
        self.processes = []
        self.cwd = "..\\Resource\\"
        
    def kill_all_process(self):
        for process in self.processes:
            process.kill()
            
        self.processes.clear()
        
    def start_new_process(self):
        if self.get_number_of_processes() == 0:
            self.update()
    
        self.processes.append(self.start_a_new_process(None))
    
    def get_number_of_processes(self):
        self.processes = [p for p in self.processes if p.poll() is None]
    
        return len(self.processes)
        
    def kill_and_update(self):
        if self.is_up_to_date():
            return
        
        self.kill_all_process()
        self.update()
        
    def open_ini(self):
        ini_file = self.executable[:-3] + "ini"
        os.startfile(ini_file)


# Represents a program which is part of a server (only one process concurrently, can have a dependencie)
class ProgramServer(Program):
    startuphidden = None

    @staticmethod
    def ensure_startup_exist():
        if ProgramServer.startuphidden is None:
            if os.name == 'nt':
                ProgramServer.startuphidden = subprocess.STARTUPINFO()
                ProgramServer.startuphidden.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    # Initialize the program
    def __init__(self, name, executable, source, timeout, hide=True):
        Program.__init__(self, "..\\Program\\" + executable, source)
    
        # Passed properties
        self.name = name
        self.timeout = timeout
        self.hide = hide
        self.check_box = None
        self.dependencies = []
        self.reliedby = []
        self.cwd = None
        
        ProgramServer.ensure_startup_exist()
        
        # Built properties
        self.process = None
        self.cwd = "..\\Program\\"
        
    # Add a dependencie
    def add_dependencie(self, dependencie):
        self.dependencies.append(dependencie)
        dependencie.reliedby.append(self)
        
    # Returns true if a process for this program is running
    def is_running(self):
        if self.process is None:
            return False
        
        if self.process.poll() is None:
            return True
            
        self.process = None
        return False
        
    # If the process is running, kills it
    def kill(self):
        if self.process is None:
            return
        
        self.process.kill()
        self.process = None
    
    def kill_top(self):
        for relied in self.reliedby:
            relied.kill_top()
            
        if self.is_running():
            self.kill()
    
    def kill_all_process(self):
        if self.is_running():
            self.kill_top()
    
    def get_status(self):
        if not self.is_running():
            return FlyFFLauncher.STATUS_OFF
        elif self.is_up_to_date():
            return FlyFFLauncher.STATUS_STARTED
        else:
            return FlyFFLauncher.STATUS_OBSOLETE
    
    def start(self):
        restart = False
        
        for dependencie in self.dependencies:
            status = dependencie.start()
            
            if status == FlyFFLauncher.COULDNT_START:
                return FlyFFLauncher.COULDNT_START
            elif status == FlyFFLauncher.CHANGED_PROCESS:
                restart = True
        
        if not self.is_up_to_date():
            self.update()
            restart = True
        
        if self.is_running() and not restart:
            return FlyFFLauncher.ALREADY_STARTED
        
        self.kill_top()
        
        startupinfo = ProgramServer.startuphidden if self.hide else None
        
        self.process = self.start_a_new_process(startupinfo)
        
        time.sleep(self.timeout)

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
    
        def make_output_path(name):
            return '..\\Output\\' + name + '\\Release\\' + name + '.exe'
    
        self.list = []
        self.list.append(ProgramServer('Account', 'AccountServer.exe', make_output_path('AccountServer'), 2, True))
        self.list.append(ProgramServer('Database', 'DatabaseServer.exe', make_output_path('DatabaseServer'), 2, True))
        self.list.append(ProgramServer('Core', 'CoreServer.exe', make_output_path('CoreServer'), 2, True))
        self.list.append(ProgramServer('Certifier', 'Certifier.exe', make_output_path('Certifier'), 2, True))
        self.list.append(ProgramServer('Login', 'LoginServer.exe', make_output_path('LoginServer'), 2, True))
        self.list.append(ProgramServer('Cache', 'CacheServer.exe', make_output_path('CacheServer'), 2, True))
        self.list.append(ProgramServer('WorldServer', 'WorldServer.exe', make_output_path('WorldServer'), 0, False))
        
        # Add dependencies
        for i in range(6):
            self.list[i + 1].add_dependencie(self.list[i])
    
    # Launch every process of the list
    def start(self):
        for program in self.list:
            if program.start() == FlyFFLauncher.COULDNT_START:
                return False
        return True
    
    def kill_server(self):
        for program in self.list:
            program.kill()
    
    def kill(self):
        self.kill_server()
        self.client.kill_all_process()
    
    def open_dir(self):
        os.startfile("..\\")
    
    # GUI
    def bind(self, index, function):
        self.list[index].bind(function)
        
    def bind_client(self, function):
        self.client.bind(function)
        
    def apply(self, index, function):
        function(self.list[index])
        
    def apply_client(self, function):
        function(self.client)
        
    def use_binds(self):
        for program in self.list:
            program.use_bind()
        
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
    
    # Server
    status_text = {
        FlyFFLauncher.STATUS_STARTED: "ON",
        FlyFFLauncher.STATUS_OFF: "OFF",
        FlyFFLauncher.STATUS_OBSOLETE: "UPDATE"
    }
    
    status_color = {
        FlyFFLauncher.STATUS_STARTED: "#005000",
        FlyFFLauncher.STATUS_OFF: "#FF0000",
        FlyFFLauncher.STATUS_OBSOLETE: "#FF8000"
    }
    
    def bind_line(index, box_name, box_status, check_box):
        def copy_name(program):
            box_name.configure(text=program.name)
            
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
            box_name.configure(foreground=status_color.get(program.get_status(), "black"))
            box_status.configure(text=status_text.get(program.get_status(), "Unknown"))
            box_status.configure(foreground=status_color.get(program.get_status(), "black"))
    
        flyff.apply(index, copy_name)
        flyff.bind(index, write_status)
        
    bind_line(0, interface.ServMsg01, interface.ServState01, interface.ServCbx01)
    bind_line(1, interface.ServMsg02, interface.ServState02, interface.ServCbx02)
    bind_line(2, interface.ServMsg03, interface.ServState03, interface.ServCbx03)
    bind_line(3, interface.ServMsg04, interface.ServState04, interface.ServCbx04)
    bind_line(4, interface.ServMsg05, interface.ServState05, interface.ServCbx05)
    bind_line(5, interface.ServMsg06, interface.ServState06, interface.ServCbx06)
    bind_line(6, interface.ServMsg07, interface.ServState07, interface.ServCbx07)
    
    def start_in_new_thread():
        from threading import Thread
        
        class StartingThread(Thread):
            def __init__(self):
                Thread.__init__(self)
    
            def run(self):
                interface.ServStart.configure(state=tk.DISABLED)
                interface.ServStop.configure(state=tk.DISABLED)
                flyff.start()
                interface.ServStart.configure(state=tk.NORMAL)
                interface.ServStop.configure(state=tk.NORMAL)
    
        thread = StartingThread()
        thread.start()
    
    interface.ServStart.configure(command=start_in_new_thread)
    interface.ServStop.configure(command=flyff.kill_server)
    
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
    interface.ClientUpdate.configure(command=flyff.client.kill_and_update)
    interface.ClientKill.configure(command=flyff.client.kill_all_process)
    interface.ClientIni.configure(command=flyff.client.open_ini)
    
    # Apply binds
    def perpetual():
        flyff.use_binds()
        root.after(1000, perpetual)
        
    perpetual()
