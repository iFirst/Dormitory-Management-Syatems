__author__ = 'Phawitch & Tanawit'
import hid
import time
import mysql.connector
import datetime

class Domdatabase():

    def __init__(self):
        #print "Test"
        #self.server = DomServer()
        self.config = {
                          'user': 'newuser',
                          'password': '12345678',
                          'host': '128.199.175.155',
                          'port': '3306',
                          'database': 'DormitoryManagementSystem',
                          'raise_on_warnings': True,
                      }
        try:
            self.con = mysql.connector.connect(**self.config)
        except Exception,e:
            raise Exception(e);
        #print "Test2"

            #raise Exception("Can't connect database.");

    #=============================Find Dorm_id and Room_Status==================================
    def queryDormAndStatus(self,Room_id):
        #print("111111");
        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        query = ("SELECT Room_Status, Dorm_id FROM Room "
        "WHERE Room_id = %d ") % (Room_id)
        curA.execute(query, (int(Room_id)))
        results = curA.fetchall()
        for row in results:
            Status = row[0]
            ID = row[1]
            (Status,ID)
        curA.close()
        self.con.close()
        return (Status,ID)

    #=====================================Find Expire Date========================================
    def queryDate(self,Room_id):
        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        query = ("SELECT ExpiryDate FROM Bill "
        "WHERE Room_id = %d ") % (Room_id)
        curA.execute(query, (int(Room_id)))
        results = curA.fetchall()
        for row in results:
            ExDate = row[0]
            (ExDate)
        curA.close()
        self.con.close()
        return (ExDate)

    #=====================================Find Door Message========================================
    def queryMessage(self,ID,Status):

        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        query = ("SELECT Content FROM Message WHERE Dorm_id = '%s' AND Status = %s ") % (ID,Status)

        curA.execute(query)
        results = curA.fetchall()

        for row in results:

            Message = row[0]

        curA.close()
        self.con.close()
        print Message;
        return (Message)

    #=====================================Find NFC Message========================================
    def queryNFCMessage(self,ID,Mac):

        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        query = ("SELECT Text FROM Machine WHERE Dorm_id = '%s' AND Mac_id = %s ") % (ID,Mac)

        curA.execute(query)
        results = curA.fetchall()

        for row in results:

            Text = row[0]

        curA.close()
        self.con.close()
        print Text;
        return (Text)


         #=====================================Find NFC MacID========================================
    def queryNFCMacId(self,ID,Mac):

        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        query = ("SELECT Mac_id FROM Machine WHERE Dorm_id = '%s' AND Mac_id = %d  ") % (ID,Mac)

        try:
            curA.execute(query)
            results = curA.fetchall()

            if (results == []):
                print "No Data"
                Mac_id = "No"
            else:
                for row in results:
                    Mac_id = row[0]

        except:
            print "Error: unable to fecth data"

        curA.close()
        self.con.close()


        #print Mac_id;
        return (Mac_id)

         #=====================================Find NFC LogNumber========================================
    def queryNFCLogNumber(self,Room_id,Mac):

        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        query = ("SELECT Log_number, Count FROM LogMachine WHERE Room_id = %d AND Mac_id = %d ") % (Room_id,Mac)
        try:

            curA.execute(query)
            results = curA.fetchall()
            if (results == []):
                print "No Data"
                Log = "-99"
                Count = 0
            else:
                for row in results:
                    Log = row[0]
                    Count = row[1]

        except:
            print "Error: unable to fecth data"

        curA.close()
        self.con.close()

        #print Log;
        #print Count;
        return (Log,Count)

         #=====================================Insert LogNumber========================================



    def insertNFCLog(self,Mac,Room_id,Count):

        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        #print "aaa"
        query = "INSERT INTO LogMachine(Mac_id,Room_id,Count) values('%s',%d,%d)" % (str(Mac),int(Room_id),int(Count))

        try:
            curA.execute(query)
            self.con.commit()
        except:
            print "Can not insert DB"
        curA.close()
        self.con.close()


     #=====================================Update LogNumber========================================
    def UpdateNFCLog(self,Mac,Room_id,Count):
        self.con = mysql.connector.connect(**self.config)
        curA = self.con.cursor(buffered=True)
        query = "Update LogMachine set Count= %d Where Mac_id = '%s' and Room_id = %d" % (Count,Mac,Room_id)
        try:
            curA.execute(query)
            self.con.commit()
        except:
            print "Can not update DB"
        curA.close()
        self.con.close()




    def insert(self,nodeNo,sensorNo,value):
        curA = self.con.cursor(buffered=True)
        query = "insert into sensor_log(node_id,sensor_id,value) values(%s, %s, %s)"
        data = (str(nodeNo),int(sensorNo),int(value*10))
        curA.execute(query,data)
        self.con.commit()

    def query(self):
        curA = self.con.cursor(buffered=True)
        query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")
        hire_start = datetime.date(1999, 1, 1)
        hire_end = datetime.date(1999, 12, 31)

        curA.execute(query, (hire_start, hire_end))

        for (first_name, last_name, hire_date) in curA:
          print("{}, {} was hired on {:%d %b %Y}".format(
            last_name, first_name, hire_date))

class gogoTalk:
    def __init__(self):
        self.GOGO_VEDOR_ID = 0x461
        self.GOGO_PRODUCT_ID = 0x20
        self.ENDPOINT_ID = 0

        # board types
        self.GOGOBOARD                     = 1
        self.PITOPPING                     = 2


        # category names
        self.CATEGORY_OUTPUT_CONTROL        = 0
        self.CATEGORY_MEMORY_CONTROL        = 1
        self.CATEGORY_RASPBERRY_PI_CONTROL  = 2

        # Output contorl command names
        self.CMD_PING                          = 1
        self.CMD_MOTOR_ON_OFF                  = 2
        self.CMD_MOTOR_DIRECTION               = 3
        self.CMD_MOTOR_RD                      = 4
        self.CMD_SET_POWER                     = 6
        self.CMD_SET_ACTIVE_PORTS              = 7
        self.CMD_TOGGLE_ACTIVE_PORT            = 8
        self.CMD_SET_SERVO_DUTY                = 9
        self.CMD_LED_CONTROL                   = 10
        self.CMD_BEEP                          = 11
        self.CMD_AUTORUN_STATE                 = 12
        self.CMD_LOGO_CONTROL                  = 13
        self.CMD_SYNC_RTC                      = 50
        self.CMD_READ_RTC                       = 51
        self.CMD_SHOW_SHORT_TEXT               = 60
        self.CMD_SHOW_LONG_TEXT                = 61
        self.CMD_CLEAR_SCREEN                  = 62

        self.CMD_VOICE_PLAY_PAUSE              = 70
        self.CMD_VOICE_NEXT_TRACK              = 71
        self.CMD_VOICE_PREV_TRACK              = 72
        self.CMD_VOICE_GOTO_TRACK              = 73
        self.CMD_VOICE_ERASE_ALL_TRACKS        = 74
        self.CMD_REBOOT                        = 100


        # Memory control command names
        self.MEM_LOGO_SET_POINTER               = 1
        self.MEM_SET_POINTER                    = 2
        self.MEM_WRITE                          = 3
        self.MEM_READ                           = 4

        # Raspberry Pi Commands

        self.RPI_SHUTDOWN                       = 1
        self.RPI_REBOOT                         = 2
        self.RPI_CAMERA_CONTROL                 = 10
        self.RPI_FIND_FACE_CONTROL              = 11
        self.RPI_TAKE_SNAPSHOT                  = 12

        self.RPI_WIFI_CONNECT                   = 15
        self.RPI_WIFI_DISCONNECT                = 16

        self.RPI_EMAIL_CONFIG                   = 17
        self.RPI_EMAIL_SEND                     = 18
        self.RPI_SMS_SEND                       = 19

        self.RPI_SET_TX_BUFFER                  = 20

        self.RPI_RFID_INIT                      = 25
        self.RPI_RFID_COMMAND                   = 26

        # output buffer location names
        self.ENDPOINT               = 0
        self.CATEGORY_ID            = 1
        self.CMD_ID                 = 2
        self.PARAMETER1             = 3
        self.PARAMETER2             = 4
        self.PARAMETER3             = 5
        self.PARAMETER4             = 6
        self.PARAMETER5             = 7
        self.PARAMETER6             = 8
        self.PARAMETER7             = 9


        self.TX_PACKET_SIZE = 64
        self.RX_PACKET_SIZE = 64

        self.RETRIES_ALLOWED = 5  # number of attempts to connect to HID device

        self.countNoData = 0

        # self.hidGoGo will be NULL if connection error
        try:
            self.hidGoGo = hid.device(self.GOGO_VEDOR_ID, self.GOGO_PRODUCT_ID)
        except IOError, ex:
            print ex
            self.hidGoGo = None

    def processCommand(self, command):
        print 'command ' + command
        command = command.split('::')
        del command[0]
        if command[0] == 'ledOn':
            self.ledControl(0,1)  # 0 = the default user led, 1 = 0n
        elif command[0] == 'ledOff':
            self.ledControl(0,0)  # 0 = the default user led, 0 = 0ff
        elif command[0] == 'beep':
            self.beep()
        elif command[0] == 'motorOn':
            self.mOn()
        elif command[0] == 'motorOff':
            self.mOff()
        elif command[0] == 'motorRD':
            self.mRD()
        elif command[0] == 'motorCW':
            self.mCW()
        elif command[0] == 'motorCCW':
            self.mCCW()
        elif command[0] == 'talkToMotor':
            self.talkToMotor(command[1])
        elif command[0] == 'setPower':
            self.setPower(command[1])



    def setFirmwareProgressCallback(self, function):
        self.firmwareProgressCallback = function


    def downloadLogoCode(self, logoBinaryString):
        ''' Download Logo Byte code to the gogo board

            It automatically sets the memory ponter to 0 and
            downloads the code
        '''

        print "Sent Logo mem pointer to 0"
        self.setLogoMemoryPointer(0)

        print "download the bin code"
        # send the Logo binary code

        self.writeFlashMemory(logoBinaryString)
        self.ledControl(1,0)
        self.beep()




    def setLogoMemoryPointer(self, pointer):
        ''' Set memory point to address 0.
            Note that this memeory address is relative to the
            Logo code area in the processor's flash memory.
            See setFlashMemoryPointer if you need to point to
            an absolute flash memory location
        '''
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_MEMORY_CONTROL
        cmdList[self.CMD_ID]        = self.MEM_LOGO_SET_POINTER
        cmdList[self.PARAMETER1]    = 0
        cmdList[self.PARAMETER2]    = 0
        self.sendCommand(cmdList)


    def setFlashMemoryPointer(self, pointer):
        ''' Sets memory pointer to a raw location on the processor
        '''
        #print "Set flash pointer to " + hex(pointer)
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_MEMORY_CONTROL
        cmdList[self.CMD_ID]        = self.MEM_SET_POINTER
        cmdList[self.PARAMETER1]    = pointer >> 8
        cmdList[self.PARAMETER2]    = pointer & 0xff
        self.sendCommand(cmdList)


    def writeFlashMemory(self, content):
        ''' Write content to the flash memory '''

        txLength = len(content)

        totalLoops = int(math.ceil(len(content)/ float((self.TX_PACKET_SIZE-4))))
        # loop and send data 'self.TX_PACKET_SIZE-4' bytes at a time

        for j in range(totalLoops):
            self.firmwareProgressCallback(j, totalLoops) # calls to let parent update the ui
            #self.firmwareProgressCallback.configure(maximum = totalLoops, value=j ) # calls to let parent update the ui

            #print str(j) + "/" + str(totalLoops)
            cmdList                     = [0]*self.TX_PACKET_SIZE
            cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
            cmdList[self.CATEGORY_ID]   = self.CATEGORY_MEMORY_CONTROL
            cmdList[self.CMD_ID]        = self.MEM_WRITE

            # if the content cannot fit in one packet
            if txLength > (self.TX_PACKET_SIZE-4):
                cmdList[self.PARAMETER1]    = self.TX_PACKET_SIZE-4
                txLength -= self.TX_PACKET_SIZE-4
            else:
                cmdList[self.PARAMETER1]    = txLength

            # copy the content to be transmitted to the output buffer
            for i in range(cmdList[self.PARAMETER1]):
                cmdList[4+i] = content[(j*(self.TX_PACKET_SIZE-4))+i]

            self.sendCommand(cmdList)

            # this dealy allows the processor to finish writing the
            # received content to the flash memory before receiving
            # more content
            time.sleep(0.01)

    def sendCommand(self, cmdBuffer):
        ''' Sends a command packet to the gogo board'''

        tries = 0

        while tries < self.RETRIES_ALLOWED:
            if self.hidGoGo != None:
                if self.hidGoGo.write(cmdBuffer) != len(cmdBuffer):
                    self.hidGoGo.close()
                    time.sleep(0.01)
                    print "tries = " + str(tries)
                else:
                    return 1   # success

            try:
                self.hidGoGo = hid.device(self.GOGO_VEDOR_ID, self.GOGO_PRODUCT_ID)
            except IOError, ex:
                print ex
            tries += 1

        self.hidGoGo = None
        return 0  # failed

    def readPacket(self):

        try:

            if self.hidGoGo == None:
                #print "in Read Packet - reconnecting"
                self.hidGoGo = hid.device(self.GOGO_VEDOR_ID, self.GOGO_PRODUCT_ID)


            #print "Opening device"

            #h = hid.device(0x2405, 0x000a)
            #h = hid.device(0x1941, 0x8021) # Fine Offset USB Weather Station

            #print "Manufacturer: %s" % self.hidGoGo.get_manufacturer_string()
            #print "Product: %s" % self.hidGoGo.get_product_string()
            #print "Serial No: %s" % self.hidGoGo.get_serial_number_string()

            # try non-blocking mode by uncommenting the next line
            self.hidGoGo.set_nonblocking(1) # makes read() returns 0 if input buffer is empty

            d = self.hidGoGo.read(64)

            if len(d) == 63:
                self.countNoData = 0
                output = d
                # while len(d) == 63:
                #     output = d
                #     d = self.hidGoGo.read(64)

                return output

            elif len(d) == 0:  # no data
                self.countNoData += 1
                # if error is not null, then assume connection error and attempt to re-connect
                if self.hidGoGo.error() != "":
                    self.hidGoGo.close()
                    self.hidGoGo = None
                    return -1
                elif self.countNoData > 20:
                    self.countNoData = 0
                    self.hidGoGo = None
                    return -1
                else:
                    return None

            else:
                print "unknown read packet len " + str(len(d))
                return -1

        except IOError, ex:
            #print "in Read Packet, " + str(ex)
            self.hidGoGo = None
            #return None
            return -1

    def beep(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_BEEP
        self.sendCommand(cmdList)

    def setAutorun(self, state):
        '''
        :param state: 0 = disabled, 1 = enabled
        :return: none
        '''
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_AUTORUN_STATE
        cmdList[self.PARAMETER1]    = state
        self.sendCommand(cmdList)

    def LogoControl(self, state):
        '''
        :param state: 0 = stop logo procedure, 1 = run logo procedure
        :return: none
        '''
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_LOGO_CONTROL
        cmdList[self.PARAMETER1]    = state
        self.sendCommand(cmdList)


    def SendPacket9(self):
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[1]      = 9


        #cmdLis
        self.sendCommand(cmdList)
        print  cmdList

    def SendPacket10(self,Status):
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[1]      = 10
        cmdList[2]      = Status

        #cmdLis
        self.sendCommand(cmdList)
        print  cmdList


    def SendPacket11(self,Message):
        global indexMessage
        global LoopMessage
        #print "Data Message"
        #print Message
        #print "----------------------------------------"
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID

        lenght = len(Message)

        Loop1 = lenght/20
        Loop2 = lenght % 20


        if (Loop2 != 0):
            FinalLoop = Loop1+1
        else:
            FinalLoop = Loop1

        j = indexMessage
        i = LoopMessage

        print FinalLoop
        print i

        if(i<FinalLoop):
            cmdList         = [0]*self.TX_PACKET_SIZE
            cmdList[1]      = 11
            cmdList[2]  = 20
            for index in xrange(0,20):
                #print "Pack %d" %(i)
                #print "index = %d" %(index+2)
                #print  "j = %d" %(j)
                cmdList[index+3] = Message[j]

                j = j+1
            i = i+1

            self.sendCommand(cmdList)
            print cmdList


        elif(i == FinalLoop):
            cmdList         = [0]*self.TX_PACKET_SIZE
            cmdList[1]      = 11
            cmdList[2]  = Loop2
            for index in xrange(0,Loop2):
                #print "Pack %d" %(i)
                # print "index = %d" %(index+2)
                #print  "j = %d" %(j)
                cmdList[index+3] = Message[j]

                j = j+1
            i = i+1

            self.sendCommand(cmdList)
            print  cmdList



        else:
            self.SendPacket12()
            indexMessage = 0
            LoopMessage = 1
            i = 1
            j = 0



        indexMessage = j
        LoopMessage = i


    def SendPacket12(self):
        global indexMessage
        global LoopMessage
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[1]      = 12
        #cmdLis
        self.sendCommand(cmdList)
        print  cmdList



    def SendPacket13(self):
        global indexMessage
        global LoopMessage
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[1]      = 13

        self.sendCommand(cmdList)
        print  cmdList


    def SendPacket14(self,num):
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[1]      = 14
        cmdList[2]      = num


        #cmdLis
        self.sendCommand(cmdList)
        print  cmdList

    def SendPacket00Exam(self,Message):
        print "Data Message"
        print Message
        print "----------------------------------------"
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID


        lenght = len(Message)

        #print lenght
        Loop1 = lenght/20
        Loop2 = lenght % 20

        if (Loop2 != 0):
            Loop1 = Loop1+1

        #print "Loop1= %d" %(Loop1)
        #print "Loop2= %d" %(Loop2)
        i = 1
        j = 0
        while(i<=Loop1):


            if(i<Loop1):
                cmdList         = [0]*self.TX_PACKET_SIZE
                cmdList[1]      = 11
                cmdList[2]  = 20
                for index in xrange(0,20):
                    #print "Pack %d" %(i)
                    #print "index = %d" %(index+2)
                    #print  "j = %d" %(j)
                    cmdList[index+3] = Message[j]

                    j = j+1
                i = i+1

                self.sendCommand(cmdList)
                print cmdList
                #print ("----------------------------------------")

            else:
                cmdList         = [0]*self.TX_PACKET_SIZE
                cmdList[1]      = 11
                cmdList[2]  = Loop2
                for index in xrange(0,Loop2):
                    #print "Pack %d" %(i)
                   # print "index = %d" %(index+2)
                    #print  "j = %d" %(j)
                    cmdList[index+3] = Message[j]

                    j = j+1
                i = i+1

                self.sendCommand(cmdList)
                print  cmdList
                #print ("----------------------------------------")



        #cmdLis
        cmdList         = [0]*self.TX_PACKET_SIZE
        cmdList[1]      = 11

        self.sendCommand(cmdList)
        print  cmdList




    def mOn(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_MOTOR_ON_OFF
        cmdList[self.PARAMETER1]    = 0
        cmdList[self.PARAMETER2]    = 1
        self.sendCommand(cmdList)

    def mOff(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_MOTOR_ON_OFF
        cmdList[self.PARAMETER1]    = 0
        cmdList[self.PARAMETER2]    = 0
        self.sendCommand(cmdList)

    def mCW(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_MOTOR_DIRECTION
        cmdList[self.PARAMETER1]    = 0
        cmdList[self.PARAMETER2]    = 1
        self.sendCommand(cmdList)

    def mCCW(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_MOTOR_DIRECTION
        cmdList[self.PARAMETER1]    = 0
        cmdList[self.PARAMETER2]    = 0
        self.sendCommand(cmdList)

    def mRD(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_MOTOR_RD
        cmdList[self.PARAMETER1]    = 0
        self.sendCommand(cmdList)

    def talkToMotor(self, motorBits):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_SET_ACTIVE_PORTS
        cmdList[self.PARAMETER1]    = int(motorBits)
        self.sendCommand(cmdList)

    def setPower(self, powerLevel):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_SET_POWER
        cmdList[self.PARAMETER1]    = 0  # target motors = 0 = currently selected motors
        cmdList[self.PARAMETER2]    = int(powerLevel)>>8      # highbyte
        cmdList[self.PARAMETER3]    = int(powerLevel) & 0xff  # lowbyte

        self.sendCommand(cmdList)

    def setServoDuty(self, duty):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_SET_SERVO_DUTY
        cmdList[self.PARAMETER1]    = 0  # target motors = 0 = currently selected motors
        cmdList[self.PARAMETER2]    = int(duty)>>8      # highbyte
        cmdList[self.PARAMETER3]    = int(duty) & 0xff  # lowbyte

        self.sendCommand(cmdList)

    def motorToggleA(self):
        self.toggleMotor(0)
    def motorToggleB(self):
        self.toggleMotor(1)
    def motorToggleC(self):
        self.toggleMotor(2)
    def motorToggleD(self):
        self.toggleMotor(3)

    def toggleMotor(self, motorNumber):

        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_TOGGLE_ACTIVE_PORT
        cmdList[self.PARAMETER1]    = motorNumber
        self.sendCommand(cmdList)

    def ledControl(self, ledID, onOffState):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_LED_CONTROL
        cmdList[self.PARAMETER1]    = ledID   # 0 = the default user LED
        cmdList[self.PARAMETER2]    = onOffState  # 0 = off , 1 = on
        self.sendCommand(cmdList)

    def reboot(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_REBOOT
        self.sendCommand(cmdList)

    def syncRTC(self, dateTimeList):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_SYNC_RTC
        for i in range(len(dateTimeList)):
            cmdList[self.PARAMETER1 + i] = dateTimeList[i]

        self.sendCommand(cmdList)

    def readRTC(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_READ_RTC
        self.sendCommand(cmdList)


    def showShortText(self, text):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_SHOW_SHORT_TEXT
        i=0
        for c in text:
            cmdList[self.PARAMETER1 + i]    = ord(c)
            i+=1
        cmdList[self.PARAMETER1 + i]    = 0 # terminates the string

        self.sendCommand(cmdList)

    def showLongText(self, text):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_SHOW_LONG_TEXT
        i=0
        for c in text:
            cmdList[self.PARAMETER1 + i]    = ord(c)
            i+=1
        cmdList[self.PARAMETER1 + i]    = 0 # terminates the string

        self.sendCommand(cmdList)

    def LCDclearText(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL
        cmdList[self.CMD_ID]        = self.CMD_CLEAR_SCREEN

        self.sendCommand(cmdList)

    def voiceModuleControl(self, command, trackNumber=-1):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_OUTPUT_CONTROL

        if command.lower().strip() =="play":
            cmdList[self.CMD_ID]        = self.CMD_VOICE_PLAY_PAUSE
        elif command.lower().strip() =="nexttrack":
            cmdList[self.CMD_ID]        = self.CMD_VOICE_NEXT_TRACK
        elif command.lower().strip() =="prevtrack":
            cmdList[self.CMD_ID]        = self.CMD_VOICE_PREV_TRACK
        elif command.lower().strip() =="gototrack":
            cmdList[self.CMD_ID]        = self.CMD_VOICE_GOTO_TRACK
            cmdList[self.PARAMETER1]    = trackNumber
        elif command.lower().strip() =="erasetracks":
            cmdList[self.CMD_ID]        = self.CMD_VOICE_ERASE_ALL_TRACKS
        self.sendCommand(cmdList)


    def rpiCameraControl(self, camera_on_state):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_CAMERA_CONTROL
        cmdList[self.PARAMETER1]    = camera_on_state  # 0 = off , 1 = on

        self.sendCommand(cmdList)

    def rpiFindFaceControl(self, find_face_state):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_FIND_FACE_CONTROL
        cmdList[self.PARAMETER1]    = find_face_state  # 0 = disable , 1 = enable

        self.sendCommand(cmdList)

    def rpiTakeSnapshot(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_TAKE_SNAPSHOT
        cmdList[self.PARAMETER1]    = 1  # 1 = save image, 0 = preview only

        self.sendCommand(cmdList)

    def rpiCameraPreview(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_TAKE_SNAPSHOT
        cmdList[self.PARAMETER1]    = 0  # 1 = save image, 0 = preview only

        self.sendCommand(cmdList)

    def rpiWifiConnect(self, ssid, password=None):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_WIFI_CONNECT
        if password is not None:
            parameterString = ssid + ',' + password
        else:
            parameterString = ssid + ','

        cmdList[self.PARAMETER1]    = len(parameterString)
        i = 0
        for c in parameterString:
            cmdList[self.PARAMETER2 + i] = ord(parameterString[i])
            i += 1

        self.sendCommand(cmdList)

    def rpiWifiDisonnect(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_WIFI_DISCONNECT
        self.sendCommand(cmdList)

    def rpiEmailConfig(self, email_user, email_password):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_EMAIL_CONFIG
        parameterString = email_user + ',' + email_password
        print parameterString
        cmdList[self.PARAMETER1]    = len(parameterString)
        i = 0
        for c in parameterString:
            cmdList[self.PARAMETER2 + i] = ord(parameterString[i])
            i += 1

        self.sendCommand(cmdList)

    def rpiEmailSend(self, email_recipient, email_subject, email_body):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_EMAIL_SEND
        parameterString = email_recipient + ',' +email_subject + ',' + email_body
        print parameterString
        cmdList[self.PARAMETER1]    = len(parameterString)
        i = 0
        for c in parameterString:
            cmdList[self.PARAMETER2 + i] = ord(parameterString[i])
            i += 1

        self.sendCommand(cmdList)

    def rpiSMSSend(self, sms_number, sms_message):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_SMS_SEND
        parameterString = sms_number + ',' +sms_message
        print parameterString
        cmdList[self.PARAMETER1]    = len(parameterString)
        i = 0
        for c in parameterString:
            cmdList[self.PARAMETER2 + i] = ord(parameterString[i])
            i += 1

        self.sendCommand(cmdList)

    def rpiSetRpiTxBuffer(self, index, value):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_SET_TX_BUFFER
        cmdList[self.PARAMETER1]    = index
        cmdList[self.PARAMETER2]    = value
        self.sendCommand(cmdList)

    def rpiClearScreenTappedFlag(self):
        RPI_SCREEN_TAP              = 20
        self.rpiSetRpiTxBuffer(RPI_SCREEN_TAP, 0)


    def rpiReboot(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_REBOOT
        self.sendCommand(cmdList)

    def rpiShutdown(self):
        cmdList                     = [0]*self.TX_PACKET_SIZE
        cmdList[self.ENDPOINT]      = self.ENDPOINT_ID
        cmdList[self.CATEGORY_ID]   = self.CATEGORY_RASPBERRY_PI_CONTROL
        cmdList[self.CMD_ID]        = self.RPI_SHUTDOWN
        self.sendCommand(cmdList)


class DomServer():
    def __init__(self):
        self.packetCount = 0
        self.database = Domdatabase()
        self.gogoBoard = gogoTalk()
        while True:
            self.processHIDdata()
            time.sleep(0.33)

    def processHIDdata(self):
        global gblDataRegister
        global gblRPiDataRegister
        global isSend
        gogoPacketReceived = False
        rPiPacketReceived = False
        global Room_Status
        global Message




        #Status,ID = self.database.queryDormAndStatus(0);
        #a = self.database.queryMessage(ID,1);
        #b = self.thai2List(a);
        #print b
        #self.gogoBoard.SendPacket11(b);




        # return if the board is being updated with a new firmware
        # reading from the HID line may cause errors.
        #if self.firmwareIsBeingUpdated == True:
          #  return

        data = self.gogoBoard.readPacket()


        # ===========================================
        # while still data available and no error
        # ===========================================


        # ===========================================
        # My Program
        # ===========================================






        while (data != None) and (data != -1):
            #print "--------------------------------------Have Data------------------------------------------------------"
            #print  data


            # if received a gogo packet

            if (data[0] == 10): # Bluetooth Status
                print "----------------------------------Packet 10---------------------------------------------------------"
                print data


                Room_id = self.ManageRoomId(data[1],data[2]);
                Room_id = int(Room_id);
                print  "Room_id = %d" %(Room_id);

                Status,ID = self.database.queryDormAndStatus(Room_id);
                print  "Dorm_id = %s" %(ID)
                print  "Status = %s" %(Status)

                if(Status == "empty"):
                    Room_Status = 3

                elif(Status == "paid"):
                    Room_Status = 2

                elif(Status == "notpaid"):
                    Room_Status = 0

                elif(Status == "noprice"):
                    Room_Status = 2

                elif(Status == "manualpaid"):
                    Room_Status = 2


                print  "Room Status = %d" % (Room_Status)


                Message1 = self.database.queryMessage(ID,1);
                LisMessage1 = self.thai2List(Message1);
                Message = LisMessage1
                print Message




                if (Room_Status == 0): # Close Door and Message1 and Message2
                    self.gogoBoard.SendPacket10(0); #Sendata to function Send



                if (Room_Status ==2): # Open Door and Message2
                    self.gogoBoard.SendPacket10(1); #Sendata to function Send


                if (Room_Status ==3): # error
                    print "Error: Empty Room"

                print  "------End BT Status------";

            elif (data[0] == 11): # Message
                print "----------------------------------Packet 11---------------------------------------------------------"
                print data

                if (Room_Status == 0):
                    #print "Send Message"
                    #print Message
                    self.gogoBoard.SendPacket11(Message)
                elif (Room_Status == 4):
                    self.gogoBoard.SendPacket11(Message)
                else:
                    #print "No Message"
                    self.gogoBoard.SendPacket12()

            elif data[0] == 13: # Receive NFC First Time
                print "----------------------------------Packet 13---------------------------------------------------------"
                print data

                Mac_id = self.ManageMacId(data[1],data[2]);
                Room_id = self.ManageRoomId(data[3],data[4]);


                print  "Room_id = %d" %(Room_id);
                print  "Mac_id = %d" %(Mac_id);

                Status,ID = self.database.queryDormAndStatus(Room_id);

                print  "Dorm_id = %s" %(ID);
                print  "Status = %s" %(Status);

                Text = self.database.queryNFCMessage(ID,Mac_id);
                print Text;
                LisText = self.thai2List(Text);

                Message1 = self.database.queryMessage(ID,1);
                LisMessage1 = self.thai2List(Message1);

                if(Status == "empty"):
                     Room_Status = 3

                elif(Status == "paid"):
                    Room_Status = 4

                elif(Status == "notpaid"):
                    Room_Status = 0


                elif(Status == "noprice"):
                    Room_Status = 4


                elif(Status == "manualpaid"):
                    Room_Status = 4


                print  "Room Status = %d" % (Room_Status)


                if (Room_Status == 0): # Not Paid Message
                    #self.gogoBoard.SendPacket11(LisMessage1);
                    Message = LisMessage1
                    self.gogoBoard.SendPacket13();


                if (Room_Status ==4): # Open Door and Message2
                    #self.gogoBoard.SendPacket11(LisText);
                    Message = LisText
                    self.gogoBoard.SendPacket13();

                if (Room_Status ==3): # error
                    #self.gogoBoard.SendPacket13();
                    print "Error: Empty Room"



            elif data[0] == 14: # Receive NFC Second Time
                print "----------------------------------Packet 14---------------------------------------------------------"
                print data

                Mac_id = self.ManageMacId(data[2],data[3]);
                Room_id = self.ManageRoomId(data[4],data[5]);

                print  "Room_id = %d" %(Room_id);
                print  "Mac_id = %d" %(Mac_id);

                Status,ID = self.database.queryDormAndStatus(Room_id);
                print  "Dorm_id = %s" %(ID);
                print  "Status = %s" %(Status);


                MacId = self.database.queryNFCMacId(ID,Mac_id);
                print  "Mac_Id = %s" %(MacId);


                if(Status == "notpaid"):
                    self.gogoBoard.SendPacket14(0);
                else:
                    if  (Mac_id == int(MacId)):
                        Log,Count = self.database.queryNFCLogNumber(Room_id,Mac_id)
                        print  "Log = %s" %(Log);
                        print  "Count = %d" %(Count);

                        if(Log != '-99'):
                            Count = Count+1
                            print  "Count After = %d" %(Count);
                            print  "Update";
                            self.database.UpdateNFCLog(MacId,Room_id,Count)
                            print  "Finish Update";

                        else:
                            Count = 1
                            print  "Count After = %d" %(Count);
                            print  "Insert";
                            self.database.insertNFCLog(MacId,Room_id,Count)
                            print  "Finish insert";
                        self.gogoBoard.SendPacket14(1);
                    else:
                        print "You are not stay in this dormitory"
                    print  "------End NFC Process------";






            elif (data[0] == 20): #Bluetooth
                print "----------------------------------Packet 10---------------------------------------------------------"
                #print data


                Room_id = self.ManageRoomId(data[1],data[2]);
                Room_id = int(Room_id);
                #print  "Room_id = %d" %(Room_id);

                Status,ID = self.database.queryDormAndStatus(Room_id);
                #print  "Dorm_id = %s" %(ID)
                #print  "Status = %s" %(Status)

                if(Status == "empty"):
                    Room_Status = 3

                elif(Status == "paid"):
                    Room_Status = 2

                elif(Status == "notpaid"):
                    Room_Status = 0

                elif(Status == "noprice"):
                    Room_Status = 2

                elif(Status == "manualpaid"):
                    Room_Status = 2


                print  "Room Status = %d" % (Room_Status)


                Message1 = self.database.queryMessage(ID,1);
                LisMessage1 = self.thai2List(Message1);

                #Message2 = self.database.queryMessage(ID,2);
                #LisMessage2 = self.thai2List(Message2);



                if (Room_Status == 0): # Close Door and Message1 and Message2
                    self.gogoBoard.SendPacket10(0); #Sendata to function Send
                    self.gogoBoard.SendPacket11(LisMessage1);
                    #self.gogoBoard.SendPacket11(LisMessage2);
                    self.gogoBoard.SendPacket12();



                if (Room_Status == 1): # Open Door and Message1 and Message2
                    self.gogoBoard.SendPacket10(0); #Sendata to function Send
                    self.gogoBoard.SendPacket11(LisMessage1);
                    #self.gogoBoard.SendPacket11(LisMessage2);
                    self.gogoBoard.SendPacket12();

                if (Room_Status ==2): # Open Door and Message2
                    self.gogoBoard.SendPacket10(1); #Sendata to function Send
                    #self.gogoBoard.SendPacket11(LisMessage1);
                    #self.gogoBoard.SendPacket11(LisMessage2);
                    self.gogoBoard.SendPacket12();

                if (Room_Status ==3): # error
                    self.gogoBoard.SendPacket10(0); #Sendata to function Send
                    self.gogoBoard.SendPacket12();
                    print "Error: Empty Room"

                print  "------End BT Process------";

            elif data[0] == 9: #Test
                print "----------------------------------Packet 9---------------------------------------------------------"
                print data
                self.gogoBoard.SendPacket9();


        # ===========================================
        # End My Program
        # ===========================================



                gogoPacketReceived = True
                gblDataRegister = data   # copy data to the global data register

                self.packetCount+=1
                sensorData=[]
                for i in range(8):
                    sensorData.append((gblDataRegister[1+(i*2)]<<8)+gblDataRegister[1+(i*2)+1])

                    # remove the sensor noise
                    if sensorData[i] >= 1020:
                        sensorData[i] = 1024

                # update the motor status
                activeMotors = gblDataRegister[22]
                motorOnOff = gblDataRegister[23]
                motorDirection = gblDataRegister[24]


            # if received a debugging message packet
            elif data[0] == 1:

                print ">>> " + ''.join(chr(x) for x in data[2:data[1]])

            # if received a raspberry pi packet
            elif data[0] == 2:
                rPiPacketReceived = True
                gblRPiDataRegister = data



            data = self.gogoBoard.readPacket()



        # ===========================================
        # If read normally -> update the UI
        # ===========================================

        if data == None:

            # Update GoGo UI
            if gogoPacketReceived:
                pass
            # Update Raspberry Pi UI
            if rPiPacketReceived:
                pass

        # ===========================================
        # If error
        # ===========================================

        # if error (board not connected)
        if data == -1:
            gblDataRegister = None   # clear the golbal data register
            sensorData = [0]*8
            activeMotors = 0
            motorOnOff = 0
            motorDirection =0



    def ManageRoomId (self,HB,LB):
        Room_id =  (HB<<8)+LB
        return (Room_id)

    def ManageMacId (self,HB,LB):
        Mac_id =  (HB<<8)+LB
        return (Mac_id)

    def ManageStatus (self,ExDate,Status):
        #print "ExDate= %s"%ExDate
        ExDate = str(ExDate)
        ExDate_Year = ExDate[:-6]
        ExDate_Month = ExDate[5:-3]
        ExDate_Day = ExDate[8:]
        ExDate_Year = int(ExDate_Year)
        ExDate_Month = int(ExDate_Month)
        ExDate_Day = int(ExDate_Day)
        #print ExDate_Year
        #print ExDate_Month
        #print ExDate_Day

        Today = datetime.datetime.now()
        #print "Today = %s" %Today.strftime("%Y-%m-%d")


        if Status == "notpaid" :
            if(ExDate_Year > Today.year):
                Room_Status = "1"
            else:
                if(ExDate_Year == Today.year):
                    if(ExDate_Month > Today.month):
                        Room_Status = "1"
                    else:
                        if(ExDate_Month == Today.month):
                            if(ExDate_Day > Today.day):
                                Room_Status = "1"
                            else:
                                Room_Status = "0"
                        else:
                            Room_Status = "0"
                else:
                   Room_Status = "0"
        else :
            Room_Status = "2"

        #print Room_Status

        return (Room_Status)

    def thai2List(self,Message):
        print Message
        Message = str(Message)
        uString = unicode(Message, "utf-8")
        #uString = unicode(str(Message), "cp874")


        outputList = [0] * len(uString) * 2
        i = 0
        for u in uString:
            val = ord(u)
            #print val
            outputList[i] = val >> 8
            outputList[i+1] = val & 0xff
            i+= 2

        return outputList

    def List2Thai(self,inList):

        outputList = []
        for i in range(len(inList)/2):
            outputList.append(unichr( (inList[i*2] << 8) + (inList[(i*2)+1])))

        return u''.join(outputList)








if __name__ == '__main__':
    receivedLogoByteCode = None
    gblDataRegister = None
    gblRPiDataRegister = None
    receivedCommand = None
    receivedLogoText = None
    indexMessage = 0
    LoopMessage = 1
    isSend = False
    server = DomServer()

