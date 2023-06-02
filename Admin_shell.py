import subprocess

class open_shell:
    def __init__(self):
        self.commands = []
    
    def add_command(self, command):
        self.commands.append(command)
    
    def run_commands(self):
        try:
            if not self.commands:
                print("No commands to execute.")
                return
            
            powershell_command = "Start-Process PowerShell -Verb RunAs -ArgumentList '-NoExit', '-Command', '{}'; exit".format(';'.join(self.commands))
            result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"PowerShell command failed with error code {result.returncode}")
                print(result.stderr)
                return None
            
            return result.stdout.strip()
        except FileNotFoundError:
            print("PowerShell is not available.")
            return None

class commands:
    def __init__(self):
        self.commands = []
    
    def add_command(self, command):
        self.commands.append(command)
    
    def clear_commands(self):
        self.commands = []
    
    def run_commands(self):
        try:
            powershell_commands = ";".join(self.commands)
            powershell_args = ['-NoExit', '-Command', powershell_commands]
            
            result = subprocess.run(['powershell', 'Start-Process', 'PowerShell', '-Verb', 'RunAs', '-ArgumentList'] + powershell_args, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"PowerShell commands failed with error code {result.returncode}")
                print(result.stderr)
                return None
            
            return result.stdout.strip()
        except FileNotFoundError:
            print("PowerShell is not available.")
            return None

def sample_call():
    open_shell_call = open_shell()
    open_shell_call.add_command("Get-command")
    output = open_shell_call.run_commands()
    if output:
        print(output)

def sample_call2():
    ps = commands()
    ps.add_command("$Host.UI.RawUI.BackgroundColor = [ConsoleColor]::Black;$Host.UI.RawUI.ForegroundColor = [ConsoleColor]::DarkGreen;")
    ps.add_command("set-location $home\desktop")
    ps.add_command("ipconfig")
    ps.add_command("Get-command")

    output = ps.run_commands()

    if output:
        print(output)

sample_call2()