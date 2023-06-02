import subprocess

list_inst=[]

def run_powershell_command(command):
    try:
        # Use subprocess to run PowerShell
        #result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        
        # Check for errors
        if result.returncode != 0:
            print(f"PowerShell command failed with error code {result.returncode}")
            print(result.stderr)
            return None
        
        # Return the output
        return result.stdout.strip()
    except FileNotFoundError:
        print("PowerShell is not available.")
        return None

iplist=["","","",]
ipconfig="ipconfig"#/ all"#| findstr DNS"    
command = "Get-Process | Select-Object Name, CPU"
get_cmds="Get-command"

list_inst.append(ipconfig)
list_inst.append(command)
list_inst.append(get_cmds)
#powerShell_command = "Start-Process PowerShell -Verb RunAs -ArgumentList '-Command', '{}' ".format(command)  <-----Starts the shell but closes it when you are done.
powerShell_command = "Start-Process PowerShell -Verb RunAs -ArgumentList '-NoExit', '-Command', '{}' ".format(ipconfig)  # <---Keeps your shell open after the call.

output = run_powershell_command(powerShell_command)

if output:
    print(output)


    