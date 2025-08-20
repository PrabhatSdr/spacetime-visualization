# Spacetime-visualization
Spacetime Visualization – A Python + Matplotlib 3D simulation of Einstein’s spacetime curvature with a glowing Sun, orbiting planet, gravitational lensing, and an animated curved grid.


# ✨ Features
- **Warped spacetime fabric** represented as a 3D grid.  
- **Glowing Sun** at the center creating the curvature.  
- **Orbiting planet** moving dynamically around the Sun.  
- **Gravitational lensing effect** (light ray bending near the Sun).  
- **Animated 3D view** with rotating camera angle.  

---

 # 🖼️ Preview
The animation includes:
- A glowing **Sun** at the center.  
- A **grid surface** showing how spacetime curves.  
- A small **planet orbiting** around the Sun.  
- A **bending light ray** simulating gravitational lensing.  

---

# 📦 Requirements
Make sure you have Python installed (≥3.7).  
Install dependencies using:

```bash
pip install numpy matplotlib
```

---

# ▶️ Run the Simulation
Simply run the Python script:
```bash
python spacetime_curvature.py
```

This will open a **3D animated window**.
---

# ⚡ Physics Behind the Visualization
- **Spacetime Fabric**: Curved by a massive object using `Z = -2/√R`, simulating a gravitational potential well.  
- **Sun**: Modeled as a glowing sphere with a halo.  
- **Planet Orbit**: Moves around the Sun in a circular path (`cos`, `sin`).  
- **Light Ray**: Slightly bends near the Sun, representing **gravitational lensing**.  

---

# 📖 Concept
This project is inspired by **Einstein’s General Theory of Relativity**, where:
- Mass tells spacetime how to curve.  
- Curved spacetime tells objects how to move.  
- Light follows curved spacetime, appearing bent when passing near massive bodies.  

---

# 🛠️ Technologies Used
- [NumPy](https://numpy.org/) – numerical computations  
- [Matplotlib](https://matplotlib.org/) – 3D visualization & animation  
