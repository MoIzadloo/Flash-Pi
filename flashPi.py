import subprocess as sub
import re


class overclock():
        def __init__(self):
            self.__red = '\u001b[31m'
            self.__yellow = '\u001b[33m'
            self.__temperature = sub.Popen(['vcgencmd' , 'measure_temp'],stdout=sub.PIPE,stderr=sub.STDOUT).communicate()
            self.__temp = re.findall("[0-9].\\.[0-9]",str(self.__temperature[0]))
            self.__cpuFrequency = sub.Popen(['vcgencmd', 'measure_clock' , 'arm'], stdout=sub.PIPE, stderr=sub.STDOUT).communicate()
            self.__cpuFreq = re.findall("=[0-9]*",str(self.__cpuFrequency[0]))
            self.__conf = sub.Popen(['vcgencmd' , 'get_config' , 'int'],stdout=sub.PIPE,stderr=sub.STDOUT).communicate()
            self.__gpuFrequency = re.findall("gpu_freq=[0-9]*",str(self.__conf[0]))
            print()
            self.__info = '''
            [+] CPU temperature is {} C
            [+] CPU frequency is {}
            [+] GPU frequency is {} MHz
            '''.format(self.__temp[0],str(self.__cpuFreq[0]).replace('=',''),str(self.__gpuFrequency[0]).replace("gpu_freq=",''))
            self.__menu = '''
            1- Overclock cpu only 
            2- Overclock gpu only 
            3- Overclock cpu & gpu
            4- Custom options
            5- Current configs
            6- Back to default settings 
            7- Exit
            '''
            self.__cpu = '''
            1- Cpu overclock up to 1.75 GHz
            2- Cpu overclock up to 2.0 GHz
            3- Back to menu 
            '''
            self.__gpu = '''
            1- Gpu overclock up to 550 MHz
            2- Gpu overclock up to 650 MHz
            3- Gpu overclock up to 750 MHz
            4- Back to menu 
            '''
            self.__gpuAndCpu = '''
            1- Cpu overclock up to 1.75 GHz & Gpu overclock up to 550 MHz
            2- Cpu overclock up to 1.75 GHz & Gpu overclock up to 650 MHz
            3- Cpu overclock up to 1.75 GHz & Gpu overclock up to 750 MHz
            4- Cpu overclock up to 2.0 GHz & Gpu overclock up to 550 MHz
            5- Cpu overclock up to 2.0 GHz & Gpu overclock up to 650 MHz
            6- Cpu overclock up to 2.0 GHz & Gpu overclock up to 750 MHz
            7- Back to menu 
            '''
            self.__config = '''
# For more options and information see
# http://rpf.io/configtxt
# Some settings may impact device functionality. See link above for details

# uncomment if you get no picture on HDMI for a default "safe" mode
#hdmi_safe=1

# uncomment this if your display has a black border of unused pixels visible
# and your display can output without overscan
#disable_overscan=1

# uncomment the following to adjust overscan. Use positive numbers if console
# goes off screen, and negative if there is too much border
#overscan_left=16
#overscan_right=16
#overscan_top=16
#overscan_bottom=16

# uncomment to force a console size. By default it will be display's size minus
# overscan.
#framebuffer_width=1280
#framebuffer_height=720

# uncomment if hdmi display is not detected and composite is being output
#hdmi_force_hotplug=1

# uncomment to force a specific HDMI mode (this will force VGA)
#hdmi_group=1
#hdmi_mode=1

# uncomment to force a HDMI mode rather than DVI. This can make audio work in
# DMT (computer monitor) modes
#hdmi_drive=2

# uncomment to increase signal to HDMI, if you have interference, blanking, or
# no display
#config_hdmi_boost=4

# uncomment for composite PAL
#sdtv_mode=2

#uncomment to overclock the arm. 700 MHz is the default.
#arm_freq=800

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Uncomment this to enable infrared communication.
#dtoverlay=gpio-ir,gpio_pin=17
#dtoverlay=gpio-ir-tx,gpio_pin=18

# Additional overlays and parameters are documented /boot/overlays/README

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

[pi4]
# Enable DRM VC4 V3D driver on top of the dispmanx display stack
dtoverlay=vc4-fkms-v3d
max_framebuffers=2

[all]
#dtoverlay=vc4-fkms-v3d

# NOOBS Auto-generated Settings:
            '''
            self.__banner = self.__red + '''

            _____________             ______              _____ 
            ___  __/__  /_____ __________  /_     ___________(_)
            __  /_ __  /_  __ `/_  ___/_  __ \    ___  __ \_  / 
            _  __/ _  / / /_/ /_(__  )_  / / /    __  /_/ /  /  
            /_/    /_/  \__,_/ /____/ /_/ /_/     _  .___//_/   
                                                  /_/           
                        
            ''' + self.__yellow
            def overclock(voltage = None ,cpu = None,gpu = None):
                print('\nVoltage : {}\nCPU frequency : {}\nGPU frequency : {}\n'.format(voltage,cpu,gpu))
                ask = str(input('Do you want to write these changes?\n1- Yes\n2- No\n' + self.__red + '$>' + self.__yellow))
                if  ask == '1' :

                    if gpu == None and cpu == None and voltage == None:
                        changes = ''''''

                    elif gpu == None:
                        changes = '''
over_voltage={}
arm_freq={}
                        '''.format(voltage,cpu)
                    elif cpu == None:
                        changes = '''
over_voltage={}
gpu_freq={}
                        '''.format(voltage,gpu)
                    else:
                        changes = '''
over_voltage={}
arm_freq={}
gpu_freq={}
                        '''.format(voltage,cpu,gpu)
                    write = self.__config + changes

                    with open('/boot/config.txt' , 'w+') as config:
                        config.writelines(write)

                    print('[+] changes have been done !')
                    reboot = str(input('Do you want to reboot now?\n1- Yes\n2- No\n' +self.__red + '$>' + self.__yellow))
                    if reboot == '1':
                        sub.Popen(['reboot'])





            while True:
                print(self.__banner)
                print(self.__info)
                print(self.__menu)
                menuOption = str(input(self.__red + '$>' + self.__yellow))

                if menuOption == '1' :
                    while True:
                        print(self.__cpu)
                        overclockCpu = str(input(self.__red + '$>' + self.__yellow))
                        if overclockCpu == '1' :
                            overclock(voltage= 5,cpu= 1750)
                        if  overclockCpu == '2' :
                            overclock(voltage= 6 ,cpu= 2000)
                        if  overclockCpu == '3' :
                            break
                        break
                if menuOption == '2' :
                    while True:
                        print(self.__gpu)
                        overclockGpu = str(input(self.__red + '$>' + self.__yellow))
                        if overclockGpu == '1' :
                            overclock(voltage= 4,gpu= 550)
                        if overclockGpu == '2' :
                            overclock(voltage= 5 ,gpu= 650)
                        if overclockGpu == '3' :
                            overclock(voltage= 6,gpu= 750)
                        if overclockGpu == '4' :
                            break
                        break
                if menuOption == '3' :
                    while True:
                        print(self.__gpuAndCpu)
                        overclockGpuAndCpu = str(input(self.__red + '$>' + self.__yellow))
                        if overclockGpuAndCpu == '1' :
                            overclock(voltage= 5,cpu= 1750,gpu= 550)
                        if overclockGpuAndCpu == '2' :
                            overclock(voltage= 5 ,cpu= 1750,gpu= 650)
                        if overclockGpuAndCpu == '3' :
                            overclock(voltage= 6,cpu= 1750,gpu= 750)
                        if overclockGpuAndCpu == '4' :
                            overclock(voltage=5,cpu= 2000,gpu= 550)
                        if overclockGpuAndCpu == '5' :
                            overclock(voltage=6,cpu= 2000,gpu= 650)
                        if overclockGpuAndCpu == '6' :
                            overclock(voltage=6,cpu= 2000,gpu= 750)
                        if overclockGpuAndCpu == '7' :
                            break
                        break
                if menuOption == '4' :
                        volt = input('Voltage :\n')
                        cpuFreq = input('CPU frequency :\n')
                        gpuFreq = input('GPU frequency :\n')
                        overclock(voltage= volt,cpu= cpuFreq,gpu= gpuFreq)
                if menuOption == '5':
                    print(str(self.__conf[0]).replace("b",'').replace("'",'').replace("\\n" , "\n"))
                    answer =  str(input('Do you want to continue?\n1- Yes\n2- No\n' + self.__red + '$>' + self.__yellow))
                    if answer == '2':
                        break

                if menuOption == '6':
                    overclock()

                if menuOption == '7':
                    break








def main():
    overclock()

main()