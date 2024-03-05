import numpy as np, pandas as pd
from scipy.signal import freqz, lfilter, filtfilt, butter, zpk2tf
from scipy import signal
from PyQt5.QtCore import QTimer

class Zero:
    def __init__(self, coordinates : complex, conj : bool = False):
        self.coordinates = coordinates
        self.has_conjugate= conj
        self.conj = None
    
class Pole:
    def __init__(self, coordinates : complex, conj : bool = False):
        self.coordinates = coordinates
        self.has_conjugate= conj
        self.conj = None
        
class Filter:
    def __init__(self, pole : complex = None):
        self.zeros = set()
        self.poles = set()
        if pole:
            chosen_pole = Pole(pole)
            calculated_zero = Zero(1 / pole.conjugate())
            self.poles.add(chosen_pole)
            self.zeros.add(calculated_zero)
        self.mag_response = None
        self.phase_response = None
        self.frequencies = None
        self.frequency_response = None
        self.numerator : list = []
        self.denominator : list = []

    
    def add_zero_pole(self, char : str, element):
        self.zeros.add(element) if char == 'z' else self.poles.add(element)

    def add_conjugates(self, highlighted_x, highlighted_y):
        for pole in self.poles.copy():
            if not pole.has_conjugate and pole.coordinates.real == highlighted_x and pole.coordinates.imag == highlighted_y:
                pole.has_conjugate = True
                pole_conj = Pole(pole.coordinates.conjugate(), True)
                pole.conj = pole_conj
                self.poles.add(pole_conj)
                pass
        for zero in self.zeros.copy():
            if not zero.has_conjugate and zero.coordinates.real == highlighted_x and zero.coordinates.imag == highlighted_y:
                zero.has_conjugate = True
                zer_conj = Zero(zero.coordinates.conjugate(), True)
                zero.conj = zer_conj
                self.zeros.add(zer_conj)
                pass

    def calculate_frequency_response(self):
        if len(self.zeros) == 0 and len(self.poles) == 0:
            return
        self.numerator, self.denominator = signal.zpk2tf([zero.coordinates for zero in self.zeros], [pole.coordinates for pole in self.poles], 1)
        self.frequencies, self.frequency_response = freqz(self.numerator, self.denominator)
        self.mag_response = np.abs(self.frequency_response)
        self.phase_response = np.angle(self.frequency_response)


class Signal:
    def __init__(self, real_signal_graph, filtered_signal_graph, filter_obj):
        self.y_coordinates = []
        self.x_coordinates = []
        self.graph1 = real_signal_graph
        self.graph2 = filtered_signal_graph
        self.X_Points_Plotted = 0
        self.sampling_rate = None
        self.timer = None
        self.data = None
        self.filtered_data = None
        self.filter = filter_obj
        self.filtered_y_coordinates = []
        self.temporal_resolution = 10

    def add_data(self, y):
        # After every y-coordinate, we apply the filter on the whole data till the last point plotted
        self.y_coordinates.append(y)
        self.x_coordinates = np.arange(len(self.y_coordinates))
        self.filter_signal()

    def filter_signal(self):
        if len(self.filter.zeros) == 0 and len(self.filter.poles) == 0:
            return
        if len(self.x_coordinates) < self.temporal_resolution:
            return
        
        self.filtered_y_coordinates = lfilter(self.filter.numerator, self.filter.denominator, self.y_coordinates)

    def plot_signal(self):
        self.X_Points_Plotted += 1
        self.graph1.setLimits(xMin = 0, xMax = float('inf'))
        self.graph2.setLimits(xMin = 0, xMax = float('inf'))
        self.graph1.plot(self.x_coordinates, self.y_coordinates, pen='b')
        self.graph2.plot(self.x_coordinates, np.real(self.filtered_y_coordinates), pen='r')
        if self.X_Points_Plotted < 100:
            self.graph1.getViewBox().setXRange(self.x_coordinates[0], self.x_coordinates[-1])
            self.graph2.getViewBox().setXRange(self.x_coordinates[0], self.x_coordinates[-1])
        else:
            self.graph1.getViewBox().setXRange(self.x_coordinates[self.X_Points_Plotted - 100], self.x_coordinates[-1])
            self.graph2.getViewBox().setXRange(self.x_coordinates[self.X_Points_Plotted - 100], self.x_coordinates[-1])

    def plot_updated_signal(self):
        self.graph1.setLimits(xMin=0, xMax=float('inf'))
        self.graph2.setLimits(xMin=0, xMax=float('inf'))
        self.data = self.graph1.plot(self.x_coordinates[:1], self.y_coordinates[:1], pen="b")
        self.filter_signal()
        self.filtered_data = self.graph2.plot(self.x_coordinates[:1], np.real(self.filtered_y_coordinates[:1]), pen='r')
        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.data.setData(self.x_coordinates[:self.X_Points_Plotted + 1], self.y_coordinates[:self.X_Points_Plotted + 1])
        if self.X_Points_Plotted >= self.temporal_resolution:
            self.filtered_data.setData(self.x_coordinates[:self.X_Points_Plotted + 1],
                                       np.real(self.filtered_y_coordinates[:self.X_Points_Plotted + 1]))
        self.X_Points_Plotted += 50


