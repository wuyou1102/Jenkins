import subprocess


def PrintOutput(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
    try:
        for line in iter(p.stdout.readline, b''):
            print line.rstrip()
        p.stdin.write("ping 192.168.90.1")
        p.stdin.flush()
        print p.stdout.read()

    except Exception, e:
        print e.message
    finally:
        print p.returncode


PrintOutput(['adb', 'devices'])
# PrintOutput(['ping', '192.168.90.1'])
