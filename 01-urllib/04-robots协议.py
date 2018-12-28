from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','http://www.baidu.com'))
