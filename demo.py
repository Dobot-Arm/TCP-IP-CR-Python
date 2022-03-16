from dobot_api import dobot_api_dashboard, dobot_api_feedback, MyType
from multiprocessing import Process
# import numpy as np
import time


def main(client_dashboard, client_feedback):
    # Remove alarm
    client_dashboard.ClearError()
    time.sleep(0.5)
    # Description The upper function was enabled successfully
    client_dashboard.EnableRobot()
    time.sleep(0.5)
    # Select user and Tool coordinate system 0
    client_dashboard.User(0)
    client_dashboard.Tool(0)
    # Call the JointMovJ directive
    client_feedback.JointMovJ(0, 50, 0, 0, 0, 0)
    time.sleep(5)
    client_feedback.JointMovJ(0, 30, 0, 0, 0, 0)
    time.sleep(5)
    print('!!!!!!END!!!!!!')


# The feedback information about port 30003 is displayed
def data_feedback(client_feedback):
    hasRead = 0
    while True:
        data = bytes()
        while hasRead < 1440:
            temp = client_feedback.socket_feedback.recv(1440 - hasRead)
            if len(temp) > 0:
                hasRead += len(temp)
                data += temp
        hasRead = 0

        a = np.frombuffer(data, dtype=MyType)
        if hex((a['test_value'][0])) == '0x123456789abcdef':
            print('robot_mode', a['robot_mode'])
            print('tool_vector_actual',
                  np.around(a['tool_vector_actual'], decimals=4))
            print('q_actual', np.around(a['q_actual'], decimals=4))


# Enable threads on ports 29999 and 30003
if __name__ == '__main__':
    client_dashboard = dobot_api_dashboard('192.168.5.1', 29999)
    client_feedback = dobot_api_feedback('192.168.5.1', 30003)
    p1 = Process(target=main, args=(client_dashboard, client_feedback))
    p1.start()
    p2 = Process(target=data_feedback, args=(client_feedback, ))
    p2.daemon = True
    p2.start()
    p1.join()
    client_dashboard.close()
    client_feedback.close()