import serial

def read_rfid(port, baudrate):
    try:
        # Open the serial port
        ser = serial.Serial(port, baudrate, timeout=1)

        while True:
            # Read data from the serial port
            data = ser.readline().strip().decode('utf-8')
            
            if data:
                # Process the RFID value
                print("RFID value:", data)

    except serial.SerialException as e:
        print("Serial port error:", str(e))
    except KeyboardInterrupt:
        print("RFID reader stopped.")

if __name__ == '__main__':
    # Specify the serial port and baudrate for your RFID reader
    port = 'COM3'  # Update with the correct port name
    baudrate = 9600  # Update with the correct baudrate

    # Call the function to read RFID values
    read_rfid(port, baudrate)