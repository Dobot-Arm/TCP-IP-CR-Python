import socket
from threading import Timer
import numpy as np

# Port Feedback
MyType=np.dtype([('len', np.int64, ), ('digital_input_bits', np.int64, ), 
                ('digital_outputs', np.int64, ), ('robot_mode', np.int64, ), 
                ('controller_timer', np.int64, ),('run_time', np.int64, ), 
                ('test_value', np.int64, ), ('safety_mode', np.float64, ), 
                ('speed_scaling', np.float64, ), ('linear_momentum_norm', np.float64, ),
                ('v_main', np.float64, ), ('v_robot', np.float64, ), 
                ('i_robot', np.float64, ), ('program_state', np.float64, ), 
                ('safety_status', np.float64, ), ('tool_accelerometer_values', np.float64, (3,)), 
                ('elbow_position', np.float64, (3,)), ('elbow_velocity', np.float64, (3,)), 
                ('q_target', np.float64, (6,)), ('qd_target', np.float64,(6,)),
                ('qdd_target', np.float64, (6,)), ('i_target', np.float64,(6,)), 
                ('m_target', np.float64, (6,)), ('q_actual', np.float64, (6,)), 
                ('qd_actual', np.float64, (6,)), ('i_actual', np.float64, (6,)), 
                ('i_control', np.float64, (6,)), ('tool_vector_actual', np.float64, (6,)), 
                ('TCP_speed_actual', np.float64, (6,)), ('TCP_force', np.float64, (6,)),
                ('Tool_vector_target', np.float64, (6,)), ('TCP_speed_target', np.float64, (6,)), 
                ('motor_temperatures', np.float64, (6,)), ('joint_modes', np.float64, (6,)), 
                ('v_actual', np.float64, (6,)), ('dummy', np.float64, (9,6))
                ])

class dobot_api_dashboard:
    """
    Define class dobot_api_dashboard to establish a connection to Dobot
    """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket_dashboard = 0

        if self.port == 29999:
            try:     
                self.socket_dashboard = socket.socket() 
                self.socket_dashboard.connect((self.ip, self.port))
            except socket.error:
                print("Fail to setup socket connection !", socket.error)
        else:
            print("Connect to dashboard server need use port 29999 !")

    def __delete__(self):
        self.close()

    def EnableRobot(self):
        """
        Enable the robot
        """
        string = "EnableRobot()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()
        
    def DisableRobot(self):
        """
        Disabled the robot
        """
        string = "DisableRobot()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def ClearError(self):
        """
        Clear controller alarm information
        """
        string = "ClearError()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def ResetRobot(self):
        """
        Robot stop
        """
        string = "ResetRobot()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def SpeedFactor(self, speed):
        """
        Setting the Global rate   
        speed:Rate value(Value range:1~100)
        """
        string = "SpeedFactor({:d})".format(speed)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8')) 
        self.WaitReply()

    def User(self, index):
        """
        Select the calibrated user coordinate system
        index : Calibrated index of user coordinates
        """
        string = "User({:d})".format(index)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def Tool(self, index):
        """
        Select the calibrated tool coordinate system
        index : Calibrated index of tool coordinates
        """
        string = "Tool({:d})".format(index)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def RobotMode(self):
        """
        View the robot status
        """
        string = "RobotMode()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def PayLoad(self, weight, inertia):
        """
        Setting robot load
        weight : The load weight
        inertia: The load moment of inertia
        """
        string = "PayLoad({:f},{:f})".format(weight,inertia)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def DO(self, index, status):
        """
        Set digital signal output (Queue instruction)
        index : Digital output index (Value range:1~24)
        status : Status of digital signal output port(0:Low level，1:High level
        """
        string = "DO({:d},{:d})".format(index,status)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def DOExecute(self, index, status):
        """
        Set digital signal output (Instructions immediately)
        index : Digital output index (Value range:1~24)
        status : Status of digital signal output port(0:Low level，1:High level)
        """
        string = "DOExecute({:d},{:d})".format(index,status)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def ToolDO(self, index, status):
        """
        Set terminal signal output (Queue instruction)
        index : Terminal output index (Value range:1~2)
        status : Status of digital signal output port(0:Low level，1:High level)
        """
        string = "ToolDO({:d},{:d})".format(index,status)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def ToolDOExecute(self, index, status):
        """
        Set terminal signal output (Instructions immediately)
        index : Terminal output index (Value range:1~2)
        status : Status of digital signal output port(0:Low level，1:High level)
        """
        string = "ToolDOExecute({:d},{:d})".format(index,status)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def AO(self, index, val):
        """
        Set analog signal output (Queue instruction)
        index : Analog output index (Value range:1~2)
        val : Voltage value (0~10)
        """
        string = "AO({:d},{:f})".format(index,val)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def AOExecute(self, index, val):
        """
        Set analog signal output (Instructions immediately)
        index : Analog output index (Value range:1~2)
        val : Voltage value (0~10)
        """
        string = "AOExecute({:d},{:f})".format(index,val)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def AccJ(self, speed):
        """
        Set joint acceleration ratio (Only for MovJ, MovJIO, MovJR, JointMovJ commands)
        speed : Joint acceleration ratio (Value range:1~100)
        """
        string = "AccJ({:d})".format(speed)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def AccL(self, speed):
        """
        Set the coordinate system acceleration ratio (Only for MovL, MovLIO, MovLR, Jump, Arc, Circle commands)
        speed : Cartesian acceleration ratio (Value range:1~100)
        """
        string = "AccL({:d})".format(speed)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def SpeedJ(self, speed):
        """
        Set joint speed ratio (Only for MovJ, MovJIO, MovJR, JointMovJ commands)
        speed : Joint velocity ratio (Value range:1~100)
        """
        string = "SpeedJ({:d})".format(speed)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def SpeedL(self, speed):
        """
        Set the cartesian acceleration ratio (Only for MovL, MovLIO, MovLR, Jump, Arc, Circle commands)
        speed : Cartesian acceleration ratio (Value range:1~100)
        """
        string = "SpeedL({:d})".format(speed)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def Arch(self, index):
        """
        Set the Jump gate parameter index (This index contains: start point lift height, maximum lift height, end point drop height)
        index : Parameter index (Value range:0~9)
        """
        string = "Arch({:d})".format(index)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def CP(self, ratio):
        """
        Set smooth transition ratio
        ratio : Smooth transition ratio (Value range:1~100)
        """
        string = "CP({:d})".format(ratio)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def LimZ(self, value):
        """
        Set the maximum lifting height of door type parameters
        value : Maximum lifting height (Highly restricted:Do not exceed the limit position of the z-axis of the manipulator)
        """
        string = "LimZ({:d})".format(value)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def SetArmOrientation(self, r, d, n, cfg):
        """
        Set the hand command
        r : Mechanical arm direction, forward/backward (1:forward -1:backward)
        d : Mechanical arm direction, up elbow/down elbow (1:up elbow -1:down elbow)
        n : Whether the wrist of the mechanical arm is flipped (1:The wrist does not flip -1:The wrist flip)
        cfg :Sixth axis Angle identification
            (1, - 2... : Axis 6 Angle is [0,-90] is -1; [90, 180] - 2; And so on
            1, 2... : axis 6 Angle is [0,90] is 1; [90180] 2; And so on)
        """
        string = "SetArmOrientation({:d},{:d},{:d},{:d})".format(r,d,n,cfg)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def PowerOn(self):
        """
        Powering on the robot
        Note: It takes about 10 seconds for the robot to be enabled after it is powered on.
        """
        string = "PowerOn()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def RunScript(self, project_name):
        """
        Run the script file
        project_name ：Script file name
        """
        string = "RunScript({:s})".format(project_name)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def StopScript(self):
        """
        Stop scripts
        """
        string = "StopScript()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def PauseScript(self):
        """
        Pause the script
        """
        string = "PauseScript()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def ContinueScript(self):
        """
        Continue running the script
        """
        string = "ContinueScript()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def GetHoldRegs(self, id, addr, count, type):
        """
        Read hold register
        id :Secondary device NUMBER (A maximum of five devices can be supported. The value ranges from 0 to 4
            Set to 0 when accessing the internal slave of the controller)
        addr :Hold the starting address of the register (Value range:3095~4095)
        count :Reads the specified number of types of data (Value range:1~16)
        type :The data type
            If null, the 16-bit unsigned integer (2 bytes, occupying 1 register) is read by default
            "U16" : reads 16-bit unsigned integers (2 bytes, occupying 1 register)
            "U32" : reads 32-bit unsigned integers (4 bytes, occupying 2 registers)
            "F32" : reads 32-bit single-precision floating-point number (4 bytes, occupying 2 registers)
            "F64" : reads 64-bit double precision floating point number (8 bytes, occupying 4 registers)
        """
        string = "GetHoldRegs({:d},{:d},{:d},{:s})".format(id,addr,count,type)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def SetHoldRegs(self, id, addr, count, table, type):
        """
        Write hold register
        id :Secondary device NUMBER (A maximum of five devices can be supported. The value ranges from 0 to 4
            Set to 0 when accessing the internal slave of the controller)
        addr :Hold the starting address of the register (Value range:3095~4095)
        count :Writes the specified number of types of data (Value range:1~16)
        type :The data type
            If null, the 16-bit unsigned integer (2 bytes, occupying 1 register) is read by default
            "U16" : reads 16-bit unsigned integers (2 bytes, occupying 1 register)
            "U32" : reads 32-bit unsigned integers (4 bytes, occupying 2 registers)
            "F32" : reads 32-bit single-precision floating-point number (4 bytes, occupying 2 registers)
            "F64" : reads 64-bit double precision floating point number (8 bytes, occupying 4 registers)
        """
        string = "SetHoldRegs({:d},{:d},{:d},{:d},{:s})".format(id,addr,count,table,type)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def ModbusCreate(self, ip, port, slave_id, isRTU):
        """
        Create Modbus connection
        ip       : slave ip address
        port     : slave port
        slave_id : slave's ID(greater than 0)
        isRTU    : 0 or 1. 0 mean create modbusTCP, 1 mean create modbusRTU
        """
        string = "ModbusCreate({:s},{:d},{:d},{:d})".format(ip, port, slave_id, isRTU)
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def Sync(self):
        """
        Synchronization instructions
        """
        string = "Sync()"
        print(string)
        self.socket_dashboard.send(str.encode(string,'utf-8'))
        self.WaitReply()

    def WaitReply(self):
        """
        Read the return value
        """
        data = self.socket_dashboard.recv(1024)
        print('receive:', bytes.decode(data,'utf-8'))

    def close(self):
        """
        Close the port
        """
        if(self.socket_dashboard != 0):
            self.socket_dashboard.close()


class dobot_api_feedback:
    """
    Define class dobot_api_feedback to establish a connection to Dobot
    """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket_feedback = 0 

        if self.port == 30003:
            try:      
                self.socket_feedback = socket.socket() 
                self.socket_feedback.connect((self.ip, self.port))
            except socket.error:
                print("Fail to connect feedback server !", socket.error)
        else:
            print("Connect to feedback server need use port 30003 !")


    def __del__(self):
        self.close()

    def MovJ(self,  x, y, z, a, b, c):
        """
        Joint motion interface (point-to-point motion mode)
        x: A number in the Cartesian coordinate system x
        y: A number in the Cartesian coordinate system y
        z: A number in the Cartesian coordinate system z
        a: A number in the Cartesian coordinate system a
        b: A number in the Cartesian coordinate system b
        c: A number in the Cartesian coordinate system c
        """
        string = "MovJ({:f},{:f},{:f},{:f},{:f},{:f})".format(x,y,z,a,b,c)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))
    
    def MovL(self, x, y, z, a, b, c):
        """
        Coordinate system motion interface (linear motion mode)
        x: A number in the Cartesian coordinate system x
        y: A number in the Cartesian coordinate system y
        z: A number in the Cartesian coordinate system z
        a: A number in the Cartesian coordinate system a
        b: A number in the Cartesian coordinate system b
        c: a number in the Cartesian coordinate system c
        """
        string = "MovL({:f},{:f},{:f},{:f},{:f},{:f})".format(x,y,z,a,b,c)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))

    def JointMovJ(self, j1, j2, j3, j4, j5, j6):
        """
        Joint motion interface (linear motion mode)
        j1~j6:Point position values on each joint
        """
        string = "JointMovJ({:f},{:f},{:f},{:f},{:f},{:f})".format(j1,j2,j3,j4,j5,j6)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8')) 
    
    def Jump(self):
        print("待定") 

    def RelMovJ(self, offset1, offset2, offset3, offset4, offset5, offset6):
        """
        Offset motion interface (point-to-point motion mode)
        j1~j6:Point position values on each joint
        """
        string = "RelMovJ({:f},{:f},{:f},{:f},{:f},{:f})".format(offset1,offset2,offset3,offset4,offset5,offset6)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))
    
    def RelMovL(self, offsetX, offsetY, offsetZ):
        """
        Offset motion interface (point-to-point motion mode)
        x: Offset in the Cartesian coordinate system x
        y: offset in the Cartesian coordinate system y
        z: Offset in the Cartesian coordinate system Z
        """
        string = "RelMovL({:f},{:f},{:f})".format(offsetX,offsetY,offsetZ)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))

    def MovLIO(self, x, y, z, a, b, c, *dynParams):
        """
        Set the digital output port state in parallel while moving in a straight line
        x: A number in the Cartesian coordinate system x
        y: A number in the Cartesian coordinate system y
        z: A number in the Cartesian coordinate system z
        a: A number in the Cartesian coordinate system a
        b: A number in the Cartesian coordinate system b
        c: a number in the Cartesian coordinate system c
        *dynParams :Parameter Settings（Mode、Distance、Index、Status）
                    Mode :Set Distance mode (0: Distance percentage; 1: distance from starting point or target point)
                    Distance :Runs the specified distance（If Mode is 0, the value ranges from 0 to 100；When Mode is 1, if the value is positive,
                             it indicates the distance from the starting point. If the value of Distance is negative, it represents the Distance from the target point）
                    Index ：Digital output index （Value range：1~24）
                    Status ：Digital output state（Value range：0/1）
        """
        # example： MovLIO(0,50,0,0,0,0,(0,50,1,0),(1,1,2,1))
        string = "MovLIO({:f},{:f},{:f},{:f},{:f},{:f}".format(x,y,z,a,b,c)
        print(type(dynParams), dynParams)
        for params in dynParams:
            print(type(params), params)
            string = string + ",{{{:d},{:d},{:d},{:d}}}".format(params[0],params[1],params[2],params[3])
        string = string + ")"
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8')) 

    def MovJIO(self, x, y, z, a, b, c, *dynParams):
        """
        Set the digital output port state in parallel during point-to-point motion
        x: A number in the Cartesian coordinate system x
        y: A number in the Cartesian coordinate system y
        z: A number in the Cartesian coordinate system z
        a: A number in the Cartesian coordinate system a
        b: A number in the Cartesian coordinate system b
        c: a number in the Cartesian coordinate system c
        *dynParams :Parameter Settings（Mode、Distance、Index、Status）
                    Mode :Set Distance mode (0: Distance percentage; 1: distance from starting point or target point)
                    Distance :Runs the specified distance（If Mode is 0, the value ranges from 0 to 100；When Mode is 1, if the value is positive,
                             it indicates the distance from the starting point. If the value of Distance is negative, it represents the Distance from the target point）
                    Index ：Digital output index （Value range：1~24）
                    Status ：Digital output state（Value range：0/1）
        """
        # example： MovJIO(0,50,0,0,0,0,(0,50,1,0),(1,1,2,1))
        string = "MovJIO({:f},{:f},{:f},{:f},{:f},{:f}".format(x,y,z,a,b,c)
        print(string)
        print(type(dynParams), dynParams)
        for params in dynParams:
            print(type(params), params)
            string = string + ",{{{:d},{:d},{:d},{:d}}}".format(params[0],params[1],params[2],params[3])
        string = string + ")"
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))  
 
    def Arc(self, x1, y1, z1, a1, b1, c1, x2, y2, z2, a2, b2, c2):
        """
        Circular motion instruction
        x1, y1, z1, a1, b1, c1 :Is the point value of intermediate point coordinates
        x2, y2, z2, a2, b2, c2 :Is the value of the end point coordinates
        Note: This instruction should be used together with other movement instructions
        """
        string = "Arc({:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f})".format(x1,y1,z1,a1,b1,c1,x2,y2,z2,a2,b2,c2)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))

    def Circle(self, count, x1, y1, z1, a1, b1, c1, x2, y2, z2, a2, b2, c2):
        """
        Full circle motion command
        count：Run laps
        x1, y1, z1, a1, b1, c1 :Is the point value of intermediate point coordinates
        x2, y2, z2, a2, b2, c2 :Is the value of the end point coordinates
        Note: This instruction should be used together with other movement instructions
        """
        string = "Circle({:d},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f})".format(count,x1,y1,z1,a1,b1,c1,x2,y2,z2,a2,b2,c2)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))
    
    def ServoJ(self, j1, j2, j3, j4, j5, j6):
        """
        Dynamic follow command based on joint space
        j1~j6:Point position values on each joint
        """
        string = "ServoJ({:f},{:f},{:f},{:f},{:f},{:f})".format(j1,j2,j3,j4,j5,j6)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))

    def ServoP(self, x, y, z, a, b, c):
        """
        Dynamic following command based on Cartesian space
        x, y, z, a, b, c :Cartesian coordinate point value
        """
        string = "ServoP({:f},{:f},{:f},{:f},{:f},{:f})".format(x,y,z,a,b,c)
        print(string)
        self.socket_feedback.send(str.encode(string,'utf-8'))

    def WaitReply(self):
        """
        30003 Port return value
        """
        all = self.socket_feedback.recv(10240)
        data = all[0:1440]
        a = np.frombuffer(data, dtype=MyType)
        if hex((a['test_value'][0])) == '0x123456789abcdef':
            print('robot_mode', a['robot_mode'])
            print('tool_vector_actual', np.around(a['tool_vector_actual'], decimals=4))
            print('q_actual', np.around(a['q_actual'], decimals=4))
            print('test_value', a['test_value'])
       
    def close(self):
        """
        Close port
        """
        if(self.socket_feedback != 0):
            self.socket_feedback.close()
