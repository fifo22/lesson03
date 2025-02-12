import subprocess
def ping(host):
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    return 'success' if result.returncode == 0 else "doesn't work!"
print(ping('google1.com'))

#Результат:
#Если хост google.com
#success
#
#Process finished with exit code 0

#Если хост google1.com
#ping: google1.com: С именем узла не связано ни одного адреса
#doesn't work!
#
#Process finished with exit code 0