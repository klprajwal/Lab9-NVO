import subprocess

# Execute createVnet.py
print("Executing createVnet.py")
subprocess.call(["python3", "createVnet.py"])

# Execute createInstance.py
print("Executing createInstance.py")
subprocess.call(["python3", "createInstance.py"])

# Execute nsg.py
print("Executing nsg.py")
subprocess.call(["python3", "nsg.py"])