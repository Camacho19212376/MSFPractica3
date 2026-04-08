"""
Práctica: Sistema musculoesqueletico
Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Tchandra Yahoel Camacho Llanes
Número de control: 19212376
Correo institucional: l19212376@tijuana.tecnm.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x0,t0,tend,dt = 0,0,10,1e-3
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)

#SEÑAL DE ENTRADA
u_original = np.array(pd.read_excel('signal.xlsx', header=None)).flatten()

# Tiempo original de la señal
t_original = np.linspace(t0, tend, len(u_original))

# Interpolación
u = np.interp(t, t_original, u_original)

# FUNCIÓN DEL MUSCULOESQUELETICO
def musculoesqueletico(a, Cs, Cp, R):
    num = [R*Cs, (1 - a)]
    den = [R*Cp + R*Cs, 1]
    return ctrl.tf(num, den)


#COMPONENTES
a,Cs,Cp = 0.25,10e-6,100e-6

# Control
R_control = 100
sys_control = musculoesqueletico(a, Cs, Cp, R_control)

# Caso
R_caso = 10000
sys_caso = musculoesqueletico(a, Cs, Cp, R_caso)

# RESPUESTAS
_, F = ctrl.forced_response(sys_control, t, u, x0)
_, Fs = ctrl.forced_response(sys_caso, t, u, x0)

# CONTROLADOR PI
def controlador(kP, kI, sys):
    Cr = 1e-6
    Re = 1 / (kI * Cr)
    Rr = kP * Re

    numPI = [Rr*Cr, 1]
    denPI = [Re*Cr, 0]

    PI = ctrl.tf(numPI, denPI)
    sistema_total = ctrl.series(PI, sys)
    sistema_cerrado = ctrl.feedback(sistema_total, 1, sign=-1)

    return sistema_cerrado

# Parámetros PI
kP,kI = 1.896,2984.968

PI_sys = controlador(kP, kI, sys_caso)

_, PI = ctrl.forced_response(PI_sys, t, F, x0)

# GRÁFICAS
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

colors = np.array([
    [10,196,224],
    [133,64,157],
    [238,167,39]
]) / 255

#SUBPLOT 1
ax1.step(t, u, where='post', linewidth=1, color=colors[0], label='Entrada')
ax1.plot(t, F, '-', linewidth=1, color=colors[1], label='F(t): Control')

ax1.set_title('Entrada vs Control')
ax1.set_xlim(0, 10)
ax1.set_ylim(-0.2, 1.2)
ax1.set_xticks(np.arange(0, 11, 1))
ax1.set_yticks(np.arange(-0.2, 1.21, 0.2))
ax1.set_xlabel('t [s]')
ax1.set_ylabel('F(t) [V]')
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3)

#SUBPLOT 2
ax2.plot(t, F, '-', linewidth=1, color=colors[0], label='F(t): Control')
ax2.plot(t, Fs, '-', linewidth=1, color=colors[1], label='F(t): Caso')
ax2.plot(t, PI, ':', linewidth=2, color=colors[2], label='PI(t): Caso')

ax2.set_title('Control vs Caso')
ax2.set_xlim(0, 10)
ax2.set_ylim(-0.2, 1.2)
ax2.set_xticks(np.arange(0, 11, 1))
ax2.set_yticks(np.arange(-0.2, 1.21, 0.2))
ax2.set_xlabel('t [s]')
ax2.set_ylabel('F(t) [V]')
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3)

plt.tight_layout()
plt.savefig('Musculoesqueletico_python.pdf')
plt.show()