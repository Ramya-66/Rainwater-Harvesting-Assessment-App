# 🌧️ Rainwater Harvesting Assessment Application

> A web-based decision-support application that helps households and institutions assess **rooftop rainwater harvesting potential** and identify suitable water storage or groundwater recharge structures.

## Overview

The **Rainwater Harvesting Assessment Application** provides a simple way to estimate rainwater harvesting potential using location and rooftop information.

Users provide basic details such as:

*  City / Location
*  Catchment / Roof Area
*  Household Water Requirement

The application analyzes the available information and provides **personalized recommendations** for suitable rainwater harvesting structures.

## Key Features

* **Rainwater Potential Assessment**
* **Location-based rainfall data**
* **Rooftop/catchment analysis**
* **Water requirement estimation**
* **Structure recommendation**
* **Result visualization**
* **Report generation**
* **Offline-friendly functionality**
* Supports both **urban and rural** use cases

The application is designed to provide personalized recommendations for storage and recharge structures while remaining usable in low-network environments.

## How It Works

<p align="center">
  <img src="./Rainwater harvesting assessment app.png" width="500" alt="Rainwater Harvesting System Architecture">
  <br>
  <em>Fig. System Architecture</em>
</p>

## Recommended Structures

Depending on the assessment, the application can recommend suitable approaches such as:

*  Storage Tanks / Rain Barrels
*  Recharge Pits
*  Recharge Wells
*  Recharge Trenches

The decision-support module is intended to help users select an appropriate harvesting or recharge structure.

## Tech Stack

| Layer           | Technology            |
| --------------- | --------------------- |
| Frontend        | HTML, CSS, JavaScript |
| Backend         | Python, Flask         |
| API             | Flask-CORS            |
| Data Processing | Pandas                |
| Visualization   | Matplotlib, Plotly    |
| Data            | JSON + rainfall APIs  |

The proposed technical architecture uses HTML/CSS/JavaScript with a Python Flask backend, supported by Pandas, Matplotlib and Plotly.

## Data Sources

The application is designed to work with rainfall information from reliable sources, including:

* **CGWB — Central Ground Water Board**
* **IMD — India Meteorological Department**
* Government-approved rainfall APIs
* Static rainfall datasets for offline use

The project presentation identifies CGWB and IMD as key sources for groundwater recharge and rainfall information.

## 👩‍💻 Developed By

**Ramya Srinivasan**

B.Tech - Artificial Intelligence & Data Science

---

### 🌍 Build smarter. Harvest rain. Conserve water.

> *Technology can turn every rooftop into a small step toward water security.*
