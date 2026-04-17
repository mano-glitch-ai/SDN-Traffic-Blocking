# SDN Traffic Blocking using Mininet + POX

## 📌 Project Overview
This project demonstrates dynamic host blocking using Software Defined Networking (SDN). The controller monitors traffic and blocks hosts that exceed a predefined threshold.

---

## ⚙️ Technologies Used
- Mininet
- POX Controller
- Python

---

## ▶️ How to Run

### 1. Start Controller
cd ~/pox  
python3 pox.py misc.traffic_block  

### 2. Start Mininet
sudo mn --controller=remote  

### 3. Test
pingall  

### 4. Generate Traffic
h1 ping h2  
