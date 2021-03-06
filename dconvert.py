#!/usr/bin/env python
#  -*- mode:python -*-

# - Michael Eager (michael.eager@monash.edu
# - Monash Biomedical Imaging
# - (C) 2014 Michael Eager

import os
import sys
import re

from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def ReadProcpar(procparfilename):
    f = open(procparfilename, 'r')
    line = f.readline()
    procpar = {}
    while line != '':
        # parse first line in property
        tokens = line.split()
        propname = tokens[0]
        propsubtype = tokens[1]
        proptype = tokens[2]
        # parse second line in property: [number of values] [first value] ...
        line = f.readline()
        tokens = line.strip().split(None, 1)
        propnumvalues = int(tokens[0])
        # handle property values
        if proptype == '1':  # real number
            if propnumvalues == 1:
                propvalue = float(tokens[1])
            else:
                propvalue = map(float, tokens[1].split())
        elif proptype == '2':  # string
            if propnumvalues == 1:
                propvalue = tokens[1].strip('"')
            if propnumvalues > 1:
                propvalue = [tokens[1].strip('"')]
                for i in range(2, propnumvalues + 1):
                    propvalue.append(f.readline().strip('"\n"'))
        line = f.readline()  # last line in property
        line = f.readline()  # next property
        lastprop = propvalue
        procpar[propname] = propvalue
    f.seek(0)
    procpartext = f.readlines()
    return (procpar, procpartext)


def check_dir(dpath):
    print 'Checking dicom directory'
    if os.path.isdir(dpath) and os.path.exists(os.join(dpath, '0001.dcm')):
        return True
    else:
        return False


def senddaris(*args):
    try:
        daris_ID = darisid.get()
        dicom_dir = outputdir.get()
        if check_dir(dicom_dir):
            cmd = './dpush -c ' + daris_ID + ' -s mf-erc ' + dicom_dir
            os.system(cmd)
        else:
            print 'FDF2Dicom converter: Error in dicom directory - not found.'

    except ValueError:
        pass


def convert(send_button):
    try:
        import os
        input_dir = inputdir.get()
        output_dir = outputdir.get()
        thispath = os.path.dirname(os.path.abspath(__file__))
        print ('dconvert path: ' + thispath)
        cmd1 = os.path.join(thispath, 'fdf2dcm.sh') + \
            ' -i ' + input_dir + ' -o ' + output_dir
        print(cmd1)
        cmd = '(if test ${MASSIVEUSERNAME + defined} \n\
then \n\
  echo ''On Massive'' \n\
  module unload python/3.3.5-gcc \n\
  module load python \n\
fi \n\
echo ''Done''\n ' + cmd1 + ')'
        print(cmd)
        os.system(cmd)
        if check_dir(output_dir):
            send_button.foreground = "dark green"
            send_button.state = 'active'
    except ValueError:
        pass


def GetDarisID(*args):
    daris_id = ''
    try:
        procpar, procpartext = ReadProcpar(inputdir.get() + '/procpar')
        if 'name' in procpar.keys():
            if re.search('DaRIS', procpar['name']):
                daris_id = re.sub('DaRIS\^', '', procpar['name'])
    except ValueError:
        pass
    return daris_id


def loadinputdir(*args):
    dir_ = filedialog.askdirectory(
        initialdir=inputdir.get(), title="Choose FDF directory", mustexist=True)  # parent,
    if re.search('img', dir_):
        out = re.sub('img', 'dcm', dir_)
    else:
        out = dir_ + '.dcm'
    inputdir.set(dir_)
    outputdir.set(out)
    darisid.set(GetDarisID())


def loadoutputdir(*args):
    dir_ = filedialog.askdirectory(initialdir=outputdir.get(
    ), title="Choose DICOM directory", mustexist=False)  # parent,
    outputdir.set(dir_)


def toggle_debug():
    d = debug.get()
    if d == 0:
        debug.set(1)
    else:
        debug.set(0)


root = Tk()
root.title("FDF to Dicom/3.0 (MBI Agilent)")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Settings", menu=filemenu)

filemenu.add_command(label="Toggle debug", command=toggle_debug)

filemenu.add_command(label="Exit", command=root.quit)


debug = IntVar()
debug.set(1)

inputdir = StringVar()
outputdir = StringVar()
darisid = StringVar()

if re.search('img', os.getcwd()):
    out = re.sub('img', 'dcm', os.getcwd())
else:
    out = os.getcwd() + '.dcm'

inputdir.set(os.getcwd())
outputdir.set(out)


inputdir_entry = Entry(mainframe, width=25, textvariable=inputdir)
inputdir_entry.grid(column=2, row=1, sticky=(W, E))

outputdir_entry = Entry(mainframe, width=25, textvariable=outputdir)
outputdir_entry.grid(column=2, row=2, sticky=(W, E))

darisid_entry = Entry(mainframe, width=25, textvariable=darisid)
darisid_entry.grid(column=2, row=3, sticky=(W, E))

# Radiobutton(mainframe, text="Debug", variable=debug, padx=10).grid(column=1, row=4, sticky=W)

#Label(mainframe, textvariable=outputdir).grid(column=2, row=2, sticky=(W, E))
Button(mainframe, text="Choose Dir", command=loadinputdir).grid(
    column=3, row=1, sticky=W)
Button(mainframe, text="Choose Dir", command=loadoutputdir).grid(
    column=3, row=2, sticky=W)

#send_button = Button(mainframe, text="Send", command=senddaris, state='disabled', foreground="red").grid(column=3, row=3, sticky=W)
# send_button.config()
send_button = Button(mainframe, text="Send", command=senddaris,
                     state='active', foreground="red").grid(column=3, row=3, sticky=W)

Button(mainframe, text="Convert", command=convert).grid(
    column=2, row=4, sticky=E)
Button(mainframe, text="Cancel", command=root.destroy).grid(
    column=3, row=4, sticky=W)


Label(mainframe, text="Input dir (FDF img)").grid(column=1, row=1, sticky=W)
Label(mainframe, text="DCM directory").grid(column=1, row=2, sticky=E)
Label(mainframe, text="DaRIS ID").grid(column=1, row=3, sticky=E)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

inputdir_entry.focus()
root.bind(' < Return > ', convert)

root.mainloop()
