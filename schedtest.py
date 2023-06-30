import time, subprocess

def execute_shell():
  shell_command = "sh /home/renatodevops/Development/SCHEDULER_PYTHON/renew.sh"
  subprocess.run(shell_command, shell=True)

while True:
  print("Runing")
  execute_shell()
  # time.sleep(7516800)
  time.sleep(5)