import subprocess
def PrintOutput(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    try:
        for line in iter(p.stdout.readline, b''):
            print line.rstrip()
    except Exception, e:
        print e.message
    finally:
        print p.returncode

PrintOutput("sdb devices")
PrintOutput("adb devices")