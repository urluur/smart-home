from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from time import localtime, strftime
import serial

app = Flask(__name__)

def read_serial_data():
    ser = serial.Serial('/dev/ttyS0', 9600)
    s = ser.readline(100)
    x = strftime("%Y-%m-%d %H:%M:%S", localtime())
    b = s.decode('utf-8')
    data = {
        "timestamp": x,
        "raw_data": b,
        "zalogovnik1": b[1:][:-83],
        "zalogovnik2": b[4:][:-80],
        "zalogovnik3": b[7:][:-77],
        "zalogovnik4": b[10:][:-74],
        "zunanja_temp": b[13:][:-68],
        "pec_f": b[19:][:-65],
        "pec_r": b[22:][:-62],
        "bojler_f": b[25:][:-59],
        "bojler_r": b[28:][:-56],
        "bojler_pumpa": b[31:][:-54],
        "kopalnica_set": b[33:][:-51],
        "kopalnica_f": b[36:][:-48],
        "kopalnica_r": b[39:][:-45],
        "kopalnica_pumpa": b[42:][:-43],
        "sobe_set": b[44:][:-40],
        "sobe_f": b[47:][:-37],
        "sobe_r": b[50:][:-34],
        "sobe_pumpa": b[53:][:-32],
        "dnevna_set": b[55:][:-29],
        "dnevna_f": b[58:][:-26],
        "dnevna_r": b[61:][:-23],
        "dnevna_pumpa": b[64:][:-21],
        "izba_set": b[66:][:-18],
        "izba_f": b[69:][:-15],
        "izba_r": b[72:][:-12],
        "izba_pumpa": b[75:][:-10],
        "kopalnica": b[77:][:-8],
        "sobe": b[78:][:-7],
        "dnevna": b[79:][:-6],
        "izba": b[80:][:-5]
    }
    return data

@app.route('/')
def index():
    data = read_serial_data()
    return render_template('index.html', data=data)

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.form['command']
    ser = serial.Serial('/dev/ttyS0', 9600)
    ser.write(command.encode('utf-8'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)