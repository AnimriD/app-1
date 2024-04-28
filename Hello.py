import streamlit as st
import numpy as np
from neuron import h, gui
from neuron.units import ms, mV, µm
from bokeh.plotting import figure
from bokeh.io import output_file, show

h.load_file("stdrun.hoc")

class BallAndStick:
    def __init__(self, gid):
        self._gid = gid
        self._setup_morphology()
        self._setup_biophysics()

    def _setup_morphology(self):
        self.soma = h.Section(name="soma", cell=self)
        self.dend = h.Section(name="dend", cell=self)
        self.all = [self.soma, self.dend]
        self.dend.connect(self.soma)
        self.soma.L = self.soma.diam = 12.6157 * µm
        self.dend.L = 200 * µm
        self.dend.diam = 1

    def _setup_biophysics(self):
        for sec in self.all:
            sec.Ra = 100  # Axial resistance in Ohm * cm
            sec.cm = 1  # Membrane capacitance in micro Farads / cm^2
        self.soma.insert("hh")
        for seg in self.soma:
            seg.hh.gnabar = 0.12
            seg.hh.gkbar = 0.036
            seg.hh.gl = 0.003
            seg.hh.el = -54.3 * mV

        # Insert passive current in the dendrite
        self.dend.insert("pas")
        for seg in self.dend:
            seg.pas.g = 0.001  # Passive conductance in S/cm2
            seg.pas.e = -65 * mV  # Leak reversal potential

    def __repr__(self):
        return "BallAndStick[{}]".format(self._gid)

my_cell = BallAndStick(0)

# Set up recording
time = h.Vector()  # Create a NEURON vector for time
voltage = h.Vector()  # Create a NEURON vector for voltage
time.record(h._ref_t)  # Record time
voltage.record(my_cell.soma(0.5)._ref_v)  # Record voltage at the center of the soma

# Set initial conditions
h.finitialize(-65)  # Set initial membrane potential to -65 mV

# Run a simulation
h.continuerun(50)  # Run the simulation for 50 ms

# Create Bokeh plot
p = figure(title="NEURON Simulation Results", x_axis_label="Time (ms)", y_axis_label="Voltage (mV)")

# Add data to Bokeh plot
p.line(np.array(time), np.array(voltage), line_width=2)

# Display Bokeh plot in Streamlit app
st.bokeh_chart(p)
