import argparse
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.optimize import curve_fit



def plot_data(x,y, name,pointcolor,linecolor,axes, max_x):
    xseq = np.linspace(0, max(max_x), num=100, endpoint=True)
    if args.regression_type == 'exp':
        popt, pcov = curve_fit(exp_func, x, y, maxfev=100000)
        a, b, c = popt
        #axes.scatter(x, y, label=None, color=pointcolor)
        axes.plot(xseq, exp_func(xseq, a, b, c), linecolor, label=name + ' (a=%.5f, b=%.2f, c=%.2f)' % (a, b, c))
    elif args.regression_type == 'linear':
        popt, pcov = curve_fit(lin_func, x, y, maxfev=100000)
        a, b = popt
        #axes.scatter(x, y, label=None, color=pointcolor)
        axes.plot(xseq, lin_func(xseq, a, b),linecolor, label=name + ' (a=%.5f, b=%.2f)' % (a, b))
    elif args.regression_type == 'log':
        popt, pcov = curve_fit(log_func, x, y, maxfev=100000)
        a, b, c = popt
        #axes.scatter(x, y, label=None, color=pointcolor)
        axes.plot(xseq, log_func(xseq, a, b, c),linecolor, label=name+' (a=%.5f, b=%.2f, c=%.2f)' % (a, b, c))
    axes.legend()
    axes.set_xlabel('Argument')
    axes.set_ylabel('Execution Time (ms)')
    axes.set_yscale('log')
    axes.set_title(args.data_folder)

def save_plot(plotname, axes, figure):
    plot_path = os.path.join("../res/",args.data_folder,plotname+args.regression_type)
    figure.savefig(plot_path)

def exp_func(x, a, b, c):
    return a * np.exp(b * x) + c

def log_func(x, a, b, c):
    return a * np.log(b * x) + c

def lin_func(x, a, b):
    return a * x + b
def plot_all_data(x_c,y_c,x_cpp,y_cpp,x_wasm_c,y_wasm_c,x_wasm_cpp,y_wasm_cpp,x_python,y_python,x_wasm_python,y_wasm_python):
    figureC, axesC = plt.subplots()
    figureCpp, axesCpp = plt.subplots()
    figurePython, axesPython = plt.subplots()
    allfigures , allaxes = plt.subplots()
    
    #data from all language
    plot_data(x_c,y_c,'C','blue','-b',allaxes, max(x_c,x_wasm_c,x_wasm_cpp,x_wasm_c,x_python,x_wasm_python))
    plot_data(x_cpp,y_cpp,'Cpp','red','-r',allaxes, max(x_c,x_wasm_c,x_wasm_cpp,x_wasm_c,x_python,x_wasm_python))
    plot_data(x_wasm_cpp,y_wasm_cpp,'Cppwasm','magenta','.m',allaxes, max(x_c,x_wasm_c,x_wasm_cpp,x_wasm_c,x_python,x_wasm_python))
    plot_data(x_wasm_c,y_wasm_c,'Cwasm','cyan','.c',allaxes, max(x_c,x_wasm_c,x_wasm_cpp,x_wasm_c,x_python,x_wasm_python))
    plot_data(x_python,y_python,'Python','green','-g',allaxes, max(x_c,x_wasm_c,x_wasm_cpp,x_wasm_c,x_python,x_wasm_python))
    plot_data(x_wasm_python,y_wasm_python,'Pythonwasm','yellow','.y',allaxes, max(x_c,x_wasm_c,x_wasm_cpp,x_wasm_c,x_python,x_wasm_python))
    save_plot("all" + args.data_folder,allaxes,allfigures)
    
    #data for C
    plot_data(x_c,y_c,'C','blue','-b',axesC, max(x_c,x_wasm_c))
    plot_data(x_wasm_c,y_wasm_c,'Cwasm','cyan','-c',axesC, max(x_c,x_wasm_c))
    save_plot("C"+args.data_folder,axesC,figureC)

    #date for Cpp
    plot_data(x_cpp,y_cpp,'Cpp','red','-r',axesCpp,max(x_cpp,x_wasm_cpp))
    plot_data(x_wasm_cpp,y_wasm_cpp,'Cppwasm','magenta','.m',axesCpp, max(x_cpp,x_wasm_cpp) )
    save_plot("Cpp"+args.data_folder, axesCpp, figureCpp)

    #data for python
    plot_data(x_python,y_python,'Python','green','-g',axesPython, max(x_python,x_wasm_python))
    plot_data(x_wasm_python,y_wasm_python,'Pythonwasm','yellow','.y',axesPython, max(x_python,x_wasm_python))
    save_plot("Python"+args.data_folder, axesPython, figurePython)

def main(args):
    # Get the list of text files in the folder
    data_files = [f for f in os.listdir(args.data_folder) if f.endswith('.txt')]

    # initialize arrays for data without 'wasm' and with 'wasm'
    x_c = []
    y_c = []
    x_cpp = []
    y_cpp = []
    x_wasm_c = []
    y_wasm_c = []
    x_wasm_cpp = []
    y_wasm_cpp = []
    x_wasm_python = []
    y_wasm_python = []
    x_python = []
    y_python = []
    arguments = dict()
    for file in data_files:
        file_path = os.path.join(args.data_folder, file)
        data = np.loadtxt(file_path)
        x = data[:, 0]
        y = data[:, 1]
        if ('python' in file) and ('wasm' in file):
            x_wasm_python.extend(x)
            y_wasm_python.extend(y)
        elif ('python' in file):
            x_python.extend(x)
            y_python.extend(y)
        elif ('wasm' in file) and ('cpp' in file):
            x_wasm_cpp.extend(x)
            y_wasm_cpp.extend(y)
        elif 'cpp' in file:
            x_cpp.extend(x)
            y_cpp.extend(y)
        elif ('wasm' in file) and ('c' in file):
            x_wasm_c.extend(x)
            y_wasm_c.extend(y)
        elif 'c' in file:
            x_c.extend(x)
            y_c.extend(y)
    plot_all_data(x_c,y_c,x_cpp,y_cpp,x_wasm_c,y_wasm_c,x_wasm_cpp,y_wasm_cpp, x_python,y_python,x_wasm_python,y_wasm_python)


parser = argparse.ArgumentParser(description='Plot two regression lines from multiple text files')
parser.add_argument('data_folder', type=str, help='The folder containing the text files')
parser.add_argument('-r', '--regression-type', type=str, default='exp', choices=['exp', 'linear', 'log'], help='The type of regression to use')
args = parser.parse_args()

main(args)